--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: survey_data; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.survey_data (
    id integer,
    "timestamp" text,
    question_1 text,
    question_2 text,
    question_3 text,
    question_4 text,
    question_5 text,
    is_relevant text,
    object text,
    is_positive text
);


ALTER TABLE public.survey_data OWNER TO user;

--
-- Name: survey_data_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.survey_data ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.survey_data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: survey_data; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.survey_data (id, "timestamp", question_1, question_2, question_3, question_4, question_5, is_relevant, object, is_positive) FROM stdin;
1	2024-04-27 06:54:22	Прога	Сон	неа	да все заебись	спать хочу	\N	\N	\N
2	2024-04-27 07:25:04	гппрооп	рппрпро	ппрпнг	понроппр	неа	\N	\N	\N
3	2024-04-27 07+3:32:24	порпр	рлорло	ирр	ррп	вавомл	\N	\N	\N
4	2024-04-27 07+3:36:08	fdfdffd	dvdvsv	vsvsvdsv	eeffe	ffff	\N	\N	\N
5	2024-04-27 07:37:20	hkjkhjk	jkjjkh	ffff	ssfs	gggg	\N	\N	\N
6	2024-04-27 07:38:56	kjlkkl	klnlk	jjj	dfhdhdf	gfgf	\N	\N	\N
\.


--
-- Name: survey_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.survey_data_id_seq', 6, true);


--
-- Name: survey_data survey_data_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.survey_data
    ADD CONSTRAINT survey_data_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

