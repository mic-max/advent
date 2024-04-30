#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw(reduce);

$\ = "\n";

my $res = 0;
my %counts = ("red" => 12, "green" => 13, "blue" => 14);

LINE_LOOP: while (<>) {
    chomp;
    my ($game) = $_ =~ m/Game (\d+):/;
    my %mins = ("red" => 0, "green" => 0, "blue" => 0);

    while ($_ =~ /(\d+) (\w+)/g) {
        my ($quantity, $color) = ($1, $2);
        if ($quantity > $mins{$color}) {
            $mins{$color} = $quantity;
        }

        # Part 1.
        # if ($quantity > $counts{$color}) {
        #     next LINE_LOOP;
        # }
    }

    my $product = reduce { $a * $b } values %mins;
    $res += $product;

    # Part 1.
    # $res += $game;
}

print($res);
