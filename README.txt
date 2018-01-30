
Roll_no:- 16129

1> input files:
	s1.asm
	s2.asm

2> command to display object_code:
	python l2.py :- prints (symbols,object codes) made by sym3,sym4,lst2,lst3 files

3> other files:-
	sym3.py:- collects symbols from s1.asm
	sym4.py:- collects symbols from s2.asm

	lst2.py:- creates object code of s1.asm
	lst3.py:- creates object code of s2.asm

4> makefile:
	read_make.py :- if enter 1 -> runs 1st file from make
			if enter 2  before 1 ->	gives error : 1st file not executed
