
```shell
ls -tr repo | xargs -I{} wc -l repo/"{}"
```

```shell
ls *2025-08-*.txt | xargs -I {} tar -czf {}.tar.gz {}
rm *2025-08-*.txt
```

```shell
caffeinate
```