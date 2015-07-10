#!/usr/bin/env ruby

#isRoot = Process.uid.zero?
#p isRoot
#exit




require 'optparse'

# for purty output

class String
    def colorize(ansi_code)
        "\e[#{ansi_code}m#{self}\e[0m"
    end

    def red
        colorize(31)
    end

    def magenta
        colorize(35)
    end

    def green
        colorize(32)
    end
end




options = {:file => nil}
raw_options = OptionParser.new do|opts|

    opts.banner = "This script decodes a Mac OS X (10.3+) automatic login password for retrieval.\nNote that unless automatic login is active, this will _NOT_ reveal any information.\n \n Usage: #{$0} [options]"

    opts.on('-f', '--file FILE', 'File to use instead of /etc/kcpassword') do |file|
        options[:file] = file
    end 

    opts.on('-h', '--help', 'This listing.') do
        puts opts
        exit
    end

end

raw_options.parse!

# define file_to_decode as argument provided, if none, then default

if options[:file].nil?
    file_to_decode = "/etc/kcpassword"
else
    file_to_decode = options[:file]
end

# error handling

begin
    File.open(file_to_decode, 'r')
rescue SystemCallError=>e
    if e.class.name =="Errno::EACCES"
        puts "Permission denied. Please re-run as root, or in single-user mode.\n\n".red
        puts raw_options

        exit 1
    elsif e.class.name == "Errno::ENOENT"
        puts "File does not exist. Please check spelling, or verify that automatic login is on.\n\n".red
        puts raw_options
        exit 2
    end
end

# magic numbers for decoding

cipher = [ 0x7D, 0x89, 0x52, 0x23, 0xD2, 0xBC, 0xDD, 0xEA, 0xA3, 0xB9, 0x1F ]
pass = ''

# loop through XORed string bytewise

xored_pass = IO.read(file_to_decode).bytes.each_with_index do |b,i|
    break if cipher.include?(b)
    pass << [ b ^ cipher[i % cipher.size]].pack("U*")
end

system ("clear")

print "\n" + "Success!".green + "\n\n"
print pass.red
print "\n\nis the password currently configured for auto-login.\n\n"
