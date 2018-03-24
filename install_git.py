#!/bin/python
import time,os,sys
import platform as pt
from subprocess import *
def starting_welcome():
    print"============================================="
    print"This script will find the current git version.\nAnd also used to update/install git"
    print"============================================="
    print"Please wait checking the git is intalled or not?"
    time.sleep(3)
    print"\n"
    return None
def clear_screen():
    if pt.system()=="Windows":
	os.system('cls')
    else:
	os.system('clear')
def run_cmd(cmd):
    sp=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
    rt=sp.wait()
    if rt==0:
	return "Sucess"
    else:
        out,err=sp.communicate()
        print err
        print "Please rectify the error and try it"
	thank_you()
	sys.exit(2)
def install_required_packages():
    clear_screen()
    cmd1="yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel -y"
    cmd2="yum install gcc perl-ExtUtils-MakeMaker -y"
    cmd3="yum install wget -y"
    print"Please wiat installing required packages"
    print "(curl-devel expat-devel gettext-devel openssl-devel zlib-devel and gcc)...."
    run_cmd(cmd1)
    run_cmd(cmd2)
    run_cmd(cmd3)
    time.sleep(4)
    return None
def get_current_git_version():
    sp=Popen('git --version',shell=True,stdout=PIPE,stderr=PIPE)
    rt=sp.wait()
    out,err=sp.communicate()
    if rt==0:
        return out.split()[-1]
    else:
	print err
	sys.exit(1)
def thank_you():
    print "\n\nThank you for using this Script\nHave a great day\n"
    return None
def get_current_working_dir():
    sp=Popen("pwd",shell=True,stdout=PIPE,stderr=PIPE)
    rt=sp.wait()
    out,err=sp.communicate()
    if rt==0:
 	#print"out is: ",out
	return out.strip('\n').strip()
    else:
	print err
	print "please rectify it and try again"
	sys.exit(3)
def install_git():
    print "Enter url to download latest git tar ball:"
    print "(Ex:https://mirrors.edge.kernel.org/pub/software/scm/git/git-1.08.3.tar.gz)"
    url=raw_input()
    install_required_packages()
    print"\nPlease wait installing the given latest git ...."
    cmd1="wget "+url
    run_cmd(cmd1)
    tar_ball=url.split(os.sep)[-1]
    print "tar_ball is: {}".format(tar_ball)
    cmd2="tar -xzf "+tar_ball
    run_cmd(cmd2)
    cmd3=tar_ball.rstrip(".tar.gz")
    pwd=get_current_working_dir()
    cmd4=pwd +os.sep+ cmd3
    print"cmd4 is: ",cmd4
    #os.system('pwd')
    os.chdir(cmd4)
    os.system("./configure")
    os.system("make")
    os.system("make install")
    os.system("ln -s /usr/local/bin/git /bin/git")   

def update_git():
    install_git()
    return None


def user_request(version=None):
    if version==None:
        yes_no=raw_input()
        if yes_no.lower() in ["yes","no"]:
            if yes_no.lower()=="yes":
                install_git()
            else:
		thank_you()
                sys.exit(0)
        else:
            while True:
                print "Enter only yes or no"
                yes_no=raw_input()
                if yes_no.lower() in ["yes","no"]:
                    if yes_no.lower()=="yes":
                        install_git()
                        break
                    else:
			thank_you()
			sys.exit(0)

    else:
        yes_no=raw_input()
        if yes_no.lower() in ["yes","no"]:
            if yes_no.lower()=="yes":
                update_git()
            else:
		thank_you()
                sys.exit(0)
        else:
            while True:
                print "Enter only yes or no"
                yes_no=raw_input()
                if yes_no.lower() in ["yes","no"]:
                    if yes_no.lower()=="yes":
                        update_git()
                        break
		    else:
			thank_you()
			sys.exit(0)
     
  

def main():
    git_ver=get_current_git_version()
    if git_ver==None:
	print "Git is not installed\n"
	print "Do you want to install git on this host?[Enter yes or no]"
        user_request()
	print"Now git has been installed on your host."
	print"And the installed git version is {}".format(get_cureent_git_version())
	print"\n"
	thank_you()
    else:	
	print "Currently intalled git version is: {}".format(git_ver)
	print "\nDo you want to update the git on this host?[Enter yes or no]"
        user_request(git_ver)
        print "Now your update git version is:{}".format(get_current_git_version())
        print"\n"
	thank_you()

if __name__=="__main__":
    clear_screen()
    starting_welcome()
    main()
