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
	./307multigrains ; echo "$$?"
	./307multigrains -h 
	./307multigrains 10 100 10 0 200 200 200 200 200
	./307multigrains 45 41 21 63 198 259 257 231 312