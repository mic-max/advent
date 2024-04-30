#!/usr/bin/perl

use strict;
use warnings;

use List::Util qw(sum max);

# Read input in paragraph mode
$/ = '';

my @chunks = <>;
chomp @chunks;

my @sums = map { sum(split /\n/, $_) } @chunks;

# Find the max sum
print max(@sums), "\n";

# Find the top three sums and add them up
my @top = sort { $b <=> $a } @sums;
print sum(@top[0..2]), "\n";
