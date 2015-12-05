#!/usr/bin/env perl

use File::Slurp qw(read_file);

my @data = read_file('input');
my $nice = 0;
foreach my $line (@data) {
	next unless $line =~ /[aeiou].*[aeiou].*[aeiou]/; # three vowels
	next unless $line =~ /([a-z])\1/; # two same letters in a row
	next if $line =~ /(ab|cd|pq|xy)/; # doesn't contain these strings
	$nice++;
}
print "Nice 1: $nice\n";

$nice = 0;
foreach my $line (@data) {
	next unless $line =~ /(([a-z])([a-z])).*\1/; # same letters split by another letter
        next unless $line =~ /([a-z])\w\1/; # has a pair of matching letters
	$nice++
}
print "Nice 2: $nice\n";
