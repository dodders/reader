#/bin/sh

632  pipenv run pip freeze > requirements.txt
  633  bat requirements.txt
  634  pip install --target ./package
  635  pipenv run pip install --target package/
  636  man pip
  637  pip3
  638  pipenv run pip
  639  pipenv run pip install --help
  640  pipenv run pip install --target package/ -r requirements.txt
  641  ls package/
  642  rm function.zip
  643  zip -r function.zip package/
  644  zip -u function.zip *.py
  645  unzip -l function.zip
  646  rm function.zip
  647  cd package/
  648  zip -r ../function.zip .
  649  cd ..
  650  zip -u function.zip *.py
  651  man zip
  652  zip -u function.zip *.py
  653  man zip
  654  zip -u function.zip *.py
