make:
	@cp src/*.py .
	@mv main.py 307multigrains
	@chmod +x 307multigrains


clean:
	@rm -f 307multigrains
	@rm -f *.py


fclean: clean
	@rm -rf __pycache__


re: fclean make


# test: re
# 	./306radiator ; echo "$$?" # missing argument
# 	./306radiator -h
# 	./306radiator input/house.csv
# 	./306radiator input/one.csv # single task
# 	./305construction input/two.csv # double task
# 	./305construction input/two_parallel.csv # two tasks doable at the same time  ## FIXME
# # 	./305construction input/house.csv > output.txt && diff output.txt tests/expected_house.txt && rm output.txt
# 	./305construction nonexistentfilehere ; echo "$$?" # nonexistent file
# 	./305construction input/empty.csv ; echo "$$?" # empty file
# 	./305construction input/blank.csv ; echo "$$?" # blank (whitespaces) file
# 	./305construction input/invalid.csv ; echo "$$?" # invalid fields
# 	./305construction input/notenough.csv ; echo "$$?" # not enough fields unpacked
# 	./305construction input/extranewline.csv ; echo "$$?" # got an extra newline at the end (raise error or continue?)
# 	./305construction input/cyclic.csv ; echo "$$?" # got a cycle in the graph
# 	./305construction input/negduration.csv ; echo "$$?" # task has negative duration
# 	./305construction input/unknowndeps.csv ; echo "$$?" # unkown task dependencies
# # 	TODO: sorting of tasks: earliest date, duration, id