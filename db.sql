PGDMP     3            
        {           product    11.16    15.3     x           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            y           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            z           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            {           1262 	   212252525    product    DATABASE     s   CREATE DATABASE product WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
    DROP DATABASE product;
                posadmin    false            h          0 	   212252557 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          posadmin    false    203   '       j          0 	   212252567    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          posadmin    false    205   D       f          0 	   212252549    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          posadmin    false    201   a       l          0 	   212252575 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          posadmin    false    207   �       n          0 	   212252585    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          posadmin    false    209   �       p          0 	   212252593    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          posadmin    false    211   �       r          0 	   212252653    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          posadmin    false    213          d          0 	   212252539    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          posadmin    false    199          b          0 	   212252528    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          posadmin    false    197   �       s          0 	   212252685    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          posadmin    false    214   |       u          0 	   212252780    products 
   TABLE DATA           k   COPY public.products (id, product_id, name, description, colour, size, created_at, updated_at) FROM stdin;
    public          posadmin    false    216   �       �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          posadmin    false    202            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          posadmin    false    204            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 28, true);
          public          posadmin    false    200            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          posadmin    false    208            �           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);
          public          posadmin    false    206            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          posadmin    false    210            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          posadmin    false    212            �           0    0    django_content_type_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_content_type_id_seq', 7, true);
          public          posadmin    false    198            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);
          public          posadmin    false    196            �           0    0    products_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.products_id_seq', 3, true);
          public          posadmin    false    215            h      x������ � �      j      x������ � �      f   9  x�]�Mn�0F��)8A5	3�^�R� �H3Ah5�/8&��#�3~R����E7�ӏ����VF���Gm��yt��%K �tA��D`����v�����״m���5*��	��r?�� c�(Hpd�#Y���U� |ks�rW�1��BPK* �.����UU p~jS�������vpyڍmX�m���9�V���TX:+�ܹH����+�я��F���5�zs�VƓ�"�Ġg�D�	C����V	aI_���a+^���jcڱ5me��+�rF&?���/g��'�+�ׇ����x�      l      x������ � �      n      x������ � �      p      x������ � �      r      x������ � �      d   i   x�M�Q
�@����a����tC]�nB�}��--�����r-������Q��!e�ŽH��xf��tg�H��زX��x��^�o�Ij���NZNTɼ�u�X0�      b   �  x����n� ����������Y6!D�%Qq���/�u&��iL����9'���c�c����  �F��+���x��蕨+#��T0���+���g	Z�җ�2���gQp�h��{��w��p�����t�צmO	�˱�� wF�i�D�G�֛N7��5���%k`��Y��U�m輣G3�S��(������=�0�y�%�̧��إ��(������"j��b��gN��Z��H�K)�O�
W�Q�D�	��`����1�w����~�+�%/�Sx��gqa�[��,���䤌,��|���ӻ�D�r�6�`��t��_q�#kgd��S;�Լ�$���B�;I=G�`�$+(��B������G��2Ԉ���))�z
���0�g~H.�M�ӌ�cSo.�����)تZV����S�c�ƂUd`V��ۥ��z'wE�)'��֔*����/��_�Wht      s      x������ � �      u   9   x�3�424D�@���X��\��@��������P������L�� ����1P�+F��� u��     