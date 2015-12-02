#!/usr/bin/env perl

use File::Slurp qw(read_file);

my $data = read_file('input');
my $open = () = $data =~ /\(/g;
my $close = () = $data =~ /\)/g;
my $destination = $open - $close;
my $floor = 0;
my $instruction = 1;

while ($data =~ /([\(\)])/g) {
        my $in = $1;
        $floor++ if ($in =~ /\(/);
        $floor-- if ($in =~ /\)/);
        last if $floor < 0;
        $instruction++;
}
print "Open: $open\tClose: $close\tDestination: $destination\n";
print "Instruction: $instruction\n";
