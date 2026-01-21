SRC = src
OUT = outputs
SUB = submit

submission: $(SRC)/a1.ipynb $(OUT)/a1.pdf $(OUT)/cleaned.csv
# 	rm -f $(SUB)/HubertBao_169077248.zip
# 	zip -j $(SUB)/HubertBao_169077248.zip $(OUT)/* $(SRC)/*
	powershell -Command "Compress-Archive -Path $(SRC)\*,$(OUT)\a1.pdf,$(OUT)\cleaned.csv -DestinationPath $(SUB)\HubertBao_169077248.zip -Force"

$(OUT)/a1.pdf: $(SRC)/a1.ipynb | $(OUT)
	python -m nbconvert --to markdown $(SRC)/a1.ipynb --output a1.md --output-dir ./$(OUT)

$(OUT): 
	mkdir -p $(OUT)