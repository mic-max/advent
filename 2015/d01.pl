#!/usr/bin/env perl

use File::Slurp qw(read_file);

my $data = read_file('input.txt');
my $open = () = $data =~ /\(/g; # counts all ( brackets
my $close = () = $data =~ /\)/g; # counts all ) brackets
my $destination = $open - $close;
my $floor = 0;
my $instruction = 1;

while ($data =~ /([\(\)])/g) {
        my $in = $1;
        $floor++ if ($in =~ /\(/); # ( bracket
        $floor-- if ($in =~ /\)/); # ) bracket
        last if $floor < 0; # exits when floor becomes negative
        $instruction++;
}
print "Open: $open\tClose: $close\tDestination: $destination\n";
print "Instruction: $instruction\n";
