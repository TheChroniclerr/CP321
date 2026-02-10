SRC = src
OUT = outputs
SUB = submit
NAME = a2

.PHONY: submission	# prevent file literally named `submission` from being tracked 
submission: $(SUB)/HubertBao_169077248.zip

$(SUB)/HubertBao_169077248.zip: $(SRC)/$(NAME).ipynb $(OUT)/$(NAME).pdf $(OUT)/cleaned.csv
# 	rm -f $(SUB)/HubertBao_169077248.zip
# 	zip -j $(SUB)/HubertBao_169077248.zip $(OUT)/* $(SRC)/*
	powershell -Command "Compress-Archive -Path $(SRC)/$(NAME).ipynb,$(OUT)/$(NAME).pdf,$(OUT)/cleaned.csv -DestinationPath $@ -Force"

$(OUT)/$(NAME).md: $(SRC)/$(NAME).ipynb | $(OUT)
	python -m nbconvert --to markdown $< --output $(NAME).md --output-dir $(OUT)

$(OUT): 
	mkdir -p $@