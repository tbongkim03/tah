# tah
- 프로젝트 파일의 정보를 cli기반으로 조회

## USAGE

```bash
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

## Dev env setting
```bash
$ git clone <URL>
$ cd <PJT_NAME>
$ pdm install
$ [pdm test|pytest]

# option
$ pdm add -dG test pytest pytest-cov
```

### deploy
```bash
# dev branch 
- https://github.com/tbongkim03/tah.git@0.2.0/args

# main
- https://github.com/tbongkim03/tah.git
```

### ref
- https://pdm-project.org/en/latest/usage/dependency/#add-development-only-dependencies
