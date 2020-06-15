# Django 인트로

## Start Django

1. 장고 설치

   ```bash
   pip install django==2.1.15
   pip list
   ```

2.  프로젝트 생성

   ```bash
   django-admin startproject <프로젝트명>
   ```

   ```bash
   python manage.py runserver
   ```

3.  프로젝트 생성시 제공되는 파일

   - manage.py
     - 전체 django와 관련된 모든 명령어를 manage.py를 통해 실행 합니다.
   - ` __init__.py`
     - 현재 ` __init__.py` 파일이 존재하는 폴더를 하나의 프로젝트, 혹은 패키지로 인식하게 해주는 파일
   - settings.py
     - 현재 프로젝트의 전체적인 성장 및 관리를 위해 존재하는 파일
   - urls.py
     - 내 프로젝트에 접근할 수 있는 경로를 설정하기 위한 파일
   
4.  admin 생성

   ``` python
   python manage.py createsuperuser
   
   # 확인은 runserver 에서 /admin/한 후 로그인
   (admin/admin)
   ```

   