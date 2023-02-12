use Time::HiRes qw( time );
open(fh, "100MB.txt") or die "Not opening";
my $start = time();
while(<fh>){
$UPPER_STRING = uc($_);
}
my $end = time();
printf("Perl : %0.02f s\n", $end - $start);
open(w, ">", "perl.txt");
print w ("%0.02f\n", $end - $start);
close(w);