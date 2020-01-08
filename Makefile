make:
	@cp src/main.py .
	@mv main.py 307multigrains
	@chmod +x 307multigrains


clean:
	@rm -f 307multigrains
	@rm -f *.py


fclean: clean
	@rm -rf __pycache__


re: fclean make

test: re
	./307multigrains ; echo "$$?" #No arguments
	./307multigrains 1 2 ; echo "$$?" #Need more arguments
	./307multigrains 1 1 1 1 1 1 1 1 1 1; echo "$$?" #Too many arguments
	./307multigrains -1 1 1 1 1 1 1 1 1; echo "$$?" #Negative arguments
	./307multigrains 1 1 1 1 1 1 1 1 -1; echo "$$?" #Negative arguments
	./307multigrains s 1 1 1 1 1 1 1 1; echo "$$?" #Arguments must be numbers
	./307multigrains 1 1 1 1 1 1 1 1 s; echo "$$?" #Arguments must be numbers
	#./307multigrains -h 
	#./307multigrains 10 100 10 0 200 200 200 200 200
	#./307multigrains 45 41 21 63 198 259 257 231 312