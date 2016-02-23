#!/usr/bin/env ruby
require 'csv'
require 'pp'
## initializing global variables


## functions


def validate_is_file(filename)
    if ! File.file?(filename)
		puts "#{filename} does not exist. Exiting."
        exit(1)
    end
end

def validate_has_valid_header(filename)
    if `head -n1 #{filename}`.chomp != "BEGIN:VCALENDAR"
        puts "#{filename} has a corrupted or malformed iCalendar header. Exiting."
        exit(2)
    end
end

def parse_events(filename)
    start_line = []
    end_line = []
    contents = []
    vevent_list = []

    ics_file = File.open(filename,"r")

    ics_file.readlines.each_with_index do |line,index|
        contents << line
        if line.chomp == 'BEGIN:VEVENT'
            start_line << index
        elsif line.chomp == 'END:VEVENT'
            end_line << index
        end
    end

    events_sanity_check(start_line,end_line)

    i = 0
    
    while i < start_line.length
    	vevent_list <<  contents[start_line[i]..end_line[i]]
        i += 1
    end

    vevent_list.each do |vevent|
    	vevent.each do |line|
    		if line.start_with? 'DTSTART'
    			print "Start: ", line.split(':')[1].slice(9..-4), '    '
    		elsif line.start_with? 'DTEND'
    			print "End: ", line.split(':')[1].slice(9..-4), '    '
    		print "\n"
    		end
    	end
    end
    







end

def events_sanity_check(list1,list2)
    if list1.length != list2.length
        puts "Unterminated or malformed event. Exiting."
        exit(3)
    end
end

#main

ARGV.each do |arg|
	validate_is_file(arg)
    validate_has_valid_header(arg)
    parse_events(arg)
end


