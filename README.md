
```shell
ls -tr repo | xargs -I{} wc -l repo/"{}"
```

```shell
DATE=2025-08-06
for file in repo/*.$DATE.txt; do
    cp "$file" "tmp/$(basename "$file" .$DATE.txt).txt"
done
```

```shell
caffeinate
```