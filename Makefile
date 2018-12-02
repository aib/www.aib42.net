ARTICLES_IN_DIR := articles
ARTICLES_OUT_DIR := html/articles

p_articles_in = $(ARTICLES_IN_DIR)/%.pandoc
p_articles_out = $(ARTICLES_OUT_DIR)/%.html
pandoc_articles := $(patsubst $(p_articles_in),$(p_articles_out),$(wildcard $(ARTICLES_IN_DIR)/*.pandoc))

p_dots_in = $(ARTICLES_IN_DIR)/%.dot
p_dots_out = $(ARTICLES_OUT_DIR)/%.png
dots := $(patsubst $(p_dots_in),$(p_dots_out),$(wildcard $(ARTICLES_IN_DIR)/*/*.dot))

.PHONY: all
all: articles

.PHONY: clean
clean:
	$(RM) $(dots) $(pandoc_articles)

.PHONY: articles
articles: $(dots) $(pandoc_articles)

$(p_articles_out): $(p_articles_in)
	pandoc -i $< --template=templates/pandoc-html.html --css="../css/pandoc.css" -p -o $@

$(p_dots_out): $(p_dots_in)
	mkdir -p $(@D)
	dot -Tpng $< -o $@
