-- DB에 영화정보와 장르정보를 삽입하는 쿼리문입니다.

-- 기존데이터 삭제를 원하시지 않는 분은 주석처리 해주세요
DELETE FROM movies_movie;
DELETE FROM movies-genre;
DELETE FROM movies-genre-movie;
-- 삽입되는 문장입니다.
.import \\Users\\haseok\\Desktop\\pjt-final\\assets\\genre_movie.csv movies_genre_movie
.import \\Users\\haseok\\Desktop\\pjt-final\\assets\\genres.csv movies_genre
.import \\Users\\haseok\\Desktop\\pjt-final\\assets\\movies.csv movies_movie