create table diabetes_status (
diabetes_012 smallint primary key,
label text not null
);

create table genhlth(
genhlth smallint primary key,
label text not null
);

create table age(
age smallint primary key,
label text not null
);

create table education (
education smallint primary key,
label text not null
);

create table income (
income smallint primary key,
label text not null
);

create table respondent_raw (
diabetes_012 smallint,
highbp smallint,
highchol smallint,
cholcheck smallint,
bmi smallint,
smoker smallint,
stroke smallint,
heart_disease smallint, 
physactivity smallint,
fruits smallint,
veggies smallint,
hvy_alc smallint,
anyhealthcare smallint,
nodocbccost smallint,
genhlth smallint,
menthlth smallint,
physhlth smallint,
diffwalk smallint,
sex smallint,
age smallint,
education smallint,
income smallint
);

create table respondent (
respondent_id serial primary key,
diabetes_012 smallint not null references diabetes_status,
highbp smallint not null check (highbp in (0,1)),
highchol smallint not null check (highchol in (0,1)),
cholcheck smallint not null check (cholcheck in (0,1)),
bmi smallint not null,
smoker smallint not null check (smoker in (0,1)),
stroke smallint not null check (stroke in (0,1)),
heart_disease smallint not null check (heart_disease in (0,1)), 
physactivity smallint not null check (physactivity in (0,1)),
fruits smallint not null check (fruits in (0,1)),
veggies smallint not null check (veggies in (0,1)),
hvy_alc smallint not null check (hvy_alc in (0,1)),
anyhealthcare smallint not null check (anyhealthcare in (0,1)),
nodocbccost smallint not null check (nodocbccost in (0,1)),
genhlth smallint not null references genhlth,
menthlth smallint not null check (menthlth between 0 and 30),
physhlth smallint not null check (physhlth between 0 and 30),
diffwalk smallint not null check (diffwalk in (0,1)),
sex smallint not null check (sex in (0,1)),
age smallint not null references age,
education smallint not null references education,
income smallint not null references income
); 

create index idx_respondent_diabetes on respondent (diabetes_012);
create index idx_respondent_age on respondent (age);
create index idx_respondent_bmi on respondent (bmi);



insert into diabetes_status values
(0, 'No diabetes'),
(1, 'Prediabetes'),
(2, 'Diabetes');

insert into genhlth values
(1, 'Excellent'),
(2, 'Very Good'),
(3, 'Good'),
(4, 'Fair'),
(5, 'Poor');


insert into age values
(1,  '18-24'),
(2,  '25-29'),
(3,  '30-34'),
(4,  '35-39'),
(5,  '40-44'),
(6,  '45-49'),
(7,  '50-54'),
(8,  '55-59'),
(9,  '60-64'),
(10, '65-69'),
(11, '70-74'),
(12, '75-79'),
(13, '80+');

insert into education values
(1, 'Never attended / kindergarten only'),
(2, 'Grades 1-8'),
(3, 'Grades 9-11'),
(4, 'Grade 12 or GED'),
(5, 'Some college / technical school'),
(6, 'College graduate');

insert into income values
(1, '< $10K'),
(2, '< $15K'),
(3, '< $20K'),
(4, '< $25K'),
(5, '< $35K'),
(6, '< $50K'),
(7, '< $75K'),
(8, '>= $75K');


INSERT INTO respondent (
    diabetes_012, highbp, highchol, cholcheck, bmi, smoker, stroke,
    heart_disease, physactivity, fruits, veggies, hvy_alc,
    anyhealthcare, nodocbccost, genhlth, menthlth, physhlth,
    diffwalk, sex, age, education, income
)
SELECT
    diabetes_012, highbp, highchol, cholcheck, bmi, smoker, stroke,
    heart_disease, physactivity, fruits, veggies, hvy_alc,
    anyhealthcare, nodocbccost, genhlth, menthlth, physhlth,
    diffwalk, sex, age, education, income
FROM respondent_raw;


SELECT
    'respondent_raw' AS tbl, COUNT(*) AS n FROM respondent_raw
UNION ALL
SELECT 'respondent', COUNT(*) FROM respondent;