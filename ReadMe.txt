Bootstrap Page:
https://getbootstrap.com/docs/4.3/getting-started/introduction/

https://github.com/hackersandslackers/flask-sqlalchemy-tutorial

Bootstrap snippets:
https://bootsnipp.com/tags/registration#

https://stackoverflow.com/questions/33107897/cognos-substr-with-varying-lengths

IF (SUBSTR( ADDR_LINE_1_1,1,3 ) = 'Co.') THEN  [ADDR_LINE_1_1];
ELSE IF (SUBSTR( ADDR_LINE_1_2,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_1_2;
ELSE IF (SUBSTR( ADDR_LINE_1_3,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_1_3;
ELSE IF (SUBSTR( ADDR_LINE_2_1,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_2_1;
ELSE IF (SUBSTR( ADDR_LINE_2_2,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_2_2;
ELSE IF (SUBSTR( ADDR_LINE_3_1,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_3_1;
ELSE IF (SUBSTR( ADDR_LINE_3_2,1,3 ) = 'Co.') THEN $calcCounty := ADDR_LINE_3_2;