#!/usr/bin/env perl

use LWP::Simple;

my $doc = get('http://www.ithome.com.tw/security')|| die "GET failed";
foreach my $line (split("\n", $doc)) {
    print $line and last if $line =~ m/2017-08-18/;
}