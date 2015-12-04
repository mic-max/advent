#!/bin/usr/env perl

use Digest::MD5 qw(md5_hex);

my $secret = "yzbqklnj";
my $answer = 0;

while(md5_hex($secret . $answer) !~ /^000000/) {
	$answer++;
}

print "Answer: $answer\n";
