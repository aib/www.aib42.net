PANDOC := pandoc

ARTICLES_IN_DIR := articles
ARTICLES_OUT_DIR := html/articles

p_articles_in = $(ARTICLES_IN_DIR)/%.pandoc
p_articles_out = $(ARTICLES_OUT_DIR)/%.html
pandoc_articles := $(patsubst $(p_articles_in),$(p_articles_out),$(wildcard $(ARTICLES_IN_DIR)/*.pandoc))

.PHONY: all
all: articles

.PHONY: clean
clean:
	$(RM) $(pandoc_articles)

.PHONY: articles
articles: $(pandoc_articles)

$(p_articles_out): $(p_articles_in)
	$(PANDOC) -i $< -o $@
