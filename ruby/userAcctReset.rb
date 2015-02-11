#!/usr/bin/env ruby
 
require 'io/console'
require 'FileUtils'
 
 
library_folder = ENV['HOME'] + '/Library/'
username = ENV['USER']
 
 
#puts "Please enter the current user's administrative password."
#print "> "
#userPassword = STDIN.noecho(&:gets).chomp
 
#generate temp root password
 
#symbols = [('A'..'Z'), ('a'..'z'), ('1'..'9')].map { |i| i.to_a }.flatten
#tempPass = (0...50).map { symbols[rand(symbols.length)] }.join
 
# enable root user
 
#system("dsenableroot -u #{username} -p #{userPassword} -r #{tempPass}")
 
#remove login keychain

#FileUtils.mv("#{library_folder}Keychains/bloggin.keychain", "#{library_folder}Keychains/bloggin_old.keychain")

#remove setup assistant plist

#FileUtils.rm "#{library_folder}Preferences/com.apple.SetupAssistant.plist"
print "n.b. type in the temporary password that you have created when prompted. \n\n"
`pwpolicy -a apple -u apple -setpolicy "newPasswordRequired=1"`

#reset password policy
#disable root user

