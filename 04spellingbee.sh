gunzip -c ../MCB185/data/dictionary.gz | grep -E ".{4,}"| grep -E "r+" | grep -Ev "[^rzoniac]" 