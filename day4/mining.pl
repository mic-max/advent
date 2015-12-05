#!/bin/usr/env perl

use Digest::MD5 qw(md5_hex);

my $answer = 0;
my $secret = "yzbqklnj";

while(md5_hex($secret . ++$answer) !~ /^00000/){};
print "Answer: $answer\n";
