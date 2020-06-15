# Django ORM

---

## CREATE

**1.  INSERT INTO table (column1, colume2, ...) VALUES (values1, values2, ...)**

```python
# 첫 번째 방법
article = Article()
article.title = 'first'
atricle.content = 'django!'
article.save()

# 두 번째 방법
# 어느 변수에 어떤 값을 넣을건지 명시
# id가 생략되어 있을 뿐, 자동으로 생성된다.
article = Article(title ='second',content='django!')

# 세 번째 방법
Article.objects.create(title ='third',content='django!')
```



---

## Read

**2. SELECT * FROM table명 **

```python
# 전체 조회
article = Article.objects.all()

```

**3. SELECT * FROM  table명 WHERE 조건**

```python
# 특정 제목 불러오기
Article.objects.filter(title='first')
```



**4. SELECT * FROM articles_article WHERE title='first' LIMIT 1**

```	python
Article.objects.filter(title='first').first()
Article.objects.filter(title='first').last()
Article.objects.filter(title='first').[0]

```

**5. SELECT * FROM articles_article WHERE id=1 **

``` python
# 고유한 값을 이용할 때 .get을 사용
# 주의점 : 고유 값이 아닌 내용을 필터링해서 
#		  2개 이상의 값이 찾아지거나 없는 것을 가지고 오려고 하면 오류를 발생한다.
Article.objects.get(id=1)
Article.objects.get(pk=1)
```

**6. Like/ startwith / endswith **

```python
# 특정 문자열을 포함 하고 있는가?
Article.objects.filter(title__contains='fir')
Article.objects.filter(title__startswith='se')
Article.objects.filter(content__endswith='ha')

```

---

## UPDATE

**UPDATE articles_article SET title='byebye' WHERE id=1 **

``` python
# 수정
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()

```

---

## DELETE

**DELETE FROM articles_article WHERE id=1**

```python
# 삭제
article = Article.objects.get(pk=1)
article.delete()

```

