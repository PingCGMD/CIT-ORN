#d Bkb-Orn

sed -i 's/0.40000  2500 ; ORN/0.41000  3000 ; ORN/g'  `grep "0.40000  2500 ; ORN" -rl  ./PolyOC*.itp`

# d Bkb-Cit1
sed -i 's/0.34700  5000 ; CIT/0.34500  5000 ; CIT/g'  `grep "0.34700  5000 ; CIT" -rl  ./PolyOC*.itp`

# d Cit1-Cit2
sed -i 's/0.34000  5000 ; CIT/0.37500  5000 ; CIT/g'  `grep "0.34000  5000 ; CIT" -rl  ./PolyOC*.itp`

# θ Bkb-Cit1-Cit2
sed -i 's/180    25 ; CIT/145    20 ; CIT/g'  `grep "180    25 ; CIT" -rl  ./PolyOC*.itp`

