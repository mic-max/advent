#!/usr/bin/env perl

use File::Slurp qw(read_file);

my @boxes = read_file('input.txt');
my $paper = 0;
my $ribbon = 0;

foreach my $box (@boxes) {
	my @d = sort {$a <=> $b} split /x/, $box;
	# paper = surface area + area of smallest side
	$paper += (3 * $d[0] * $d[1]) + (2 * $d[1] * $d[2]) + (2 * $d[2] * $d[0]);
	# ribbon is smallest perimeter + volume
	$ribbon += 2 * ($d[0] + $d[1]) + ($d[0] * $d[1] * $d[2]);
}
print "Paper: $paper\tRibbon: $ribbon\n";
