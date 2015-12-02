#!/usr/bin/env perl

use File::Slurp qw(read_file);

my @boxes = read_file('input');
my $paper = 0;
my $ribbon = 0;

foreach my $box (@boxes) {
	my @d = sort {$a <=> $b} split /x/, $box;
	my $area = (2 * $d[0] * $d[1]) + (2 * $d[1] * $d[2]) + (2 * $d[2] * $d[0]);
	my $smallest = $d[0] * $d[1];
	my $perimeter = 2 * ($d[0] + $d[1]);
	my $volume = ($d[0] * $d[1] * $d[2]);

	$paper += $area + $smallest;
	$ribbon += $volume + $perimeter;
}

print "Paper: $paper\tRibbon: $ribbon\n";
