INSERT INTO organizations (id, name)
VALUES  (1, '학생회'),
        (2, '아대 학생회');

INSERT INTO members (id, email, is_manager, password, organization_id)
VALUES  (1, 'test@test.com', 1, 'test', 1),
        (2, 'test2@test.com', 1, 'test', 1),
        (3, 'test3@test.com', 1, 'test', 2);

INSERT INTO sports (id, name)
VALUES  (1, '축구'),
        (2, '농구');

INSERT INTO quarters (id, name, sports_id)
VALUES  (1, '전반전', 1),
        (2, '후반전', 1);

INSERT INTO leagues (id, name, is_deleted, start_at, end_at, manager_id, organization_id, max_round, in_progress_round)
VALUES  (1, '외대 월드컵', 0, '2024-03-20 00:00:00', '2024-03-24 00:00:00', 1, 1, 8, 2),
        (2, '아대 월드컵', 0, '2024-03-20 00:00:00', '2024-03-24 00:00:00', 1, 1, 16, 16);

INSERT INTO league_sports (id, league_id, sport_id) VALUES (1, 1, 1);

INSERT INTO league_teams (id, name, logo_image_url, league_id, manager_id, organization_id)
VALUES  (1, '미컴과', 'image.url', 1, 1, 1),
        (2, '영어과', 'image.url', 1, 1, 1),
        (3, '아랍어과', 'image.url', 1, 1, 1),
        (4, '인도어과', 'image.url', 1, 1, 1),
        (5, '터키어과', 'image.url', 2, 2, 2);

INSERT INTO league_team_players (id, name, description, number, league_team_id)
VALUES  (1, '미컴선수1', NULL, 11, 1),
        (2, '미컴선수2', NULL, 22, 1),
        (3, '영어선수1', NULL, 33, 2),
        (4, '영어선수2', NULL, 11, 2),
        (5, '아랍선수1', NULL, 22, 3),
        (6, '아랍선수2', NULL, 11, 3),
        (7, '인도선수1', NULL, 22, 4),
        (8, '인도선수2', NULL, 44, 4),
        (9, '미컴선수3', NULL, 55, 1),
        (10, '미컴선수4', NULL, 66, 1);

INSERT INTO games (id, name, start_time, video_id, quarter_changed_at, game_quarter, state, league_id, manager_id, sport_id, round)
VALUES  (1, '준결승', '2024-03-21 14:00:00+09:00', 'video.com', '2024-03-21 13:50:00+09:00', '후반전', 'FINISHED', 1, 1, 1, 4),
        (2, '준결승', '2024-03-21 14:00:00+09:00', 'video.com', '2024-03-21 13:50:00+09:00', '후반전', 'FINISHED', 1, 1, 1, 4),
        (3, '결승', '2024-03-22 14:00:00+09:00', NULL, '2024-03-22 14:00:00+09:00', '전반전', 'PLAYING', 1, 1, 1, 2),
        (4, '삭제 될 경기', '2024-03-22 14:00:00+09:00', NULL, '2024-03-22 14:00:00+09:00', '전반전', 'SCHEDULED', 1, 1, 1, 2);

INSERT INTO game_teams (game_id, league_team_id, cheer_count, score)
VALUES  (1, 1, 0, 3),
        (1, 2, 0, 0),
        (2, 3, 0, 0),
        (2, 4, 0, 2),
        (3, 1, 0, 2),
        (3, 4, 0, 0),
        (4, 1, 0, 2),
        (4, 4, 0, 0);

INSERT INTO lineup_players (id, game_team_id, name, description, number, is_captain)
VALUES  (1, 1, '미컴선수1', NULL, 11, 0),
        (2, 1, '미컴선수2', NULL, 22, 1),
        (3, 2, '영어선수1', NULL, 33, 0),
        (4, 2, '영어선수2', NULL, 11, 1),
        (5, 3, '아랍선수1', NULL, 22, 0),
        (6, 3, '아랍선수2', NULL, 11, 1),
        (7, 4, '인도선수1', NULL, 22, 0),
        (8, 4, '인도선수2', NULL, 44, 1),
        (9, 5, '미컴선수1', NULL, 11, 1),
        (10, 5, '미컴선수2', NULL, 22, 1),
        (11, 6, '인도선수1', NULL, 22, 1),
        (12, 6, '인도선수2', NULL, 44, 1);

INSERT INTO records (id, record_type, game_id, game_team_id, recorded_quarter_id, recorded_at)
VALUES  (1, 'score', 3, 5, 1, 31),
        (2, 'score', 3, 5, 1, 44),
        (3, 'replacement', 3, 6, 2, 3);

INSERT INTO score_records (id, score, lineup_player_id, record_id)
VALUES (1, 1, 9, 1),
        (2, 1, 9, 2);

INSERT INTO replacement_records (id, origin_lineup_player_id, replaced_lineup_player_id ,record_id)
VALUES (1, 11, 12, 3);

INSERT INTO cheer_talks (id, created_at, content, is_blocked, game_team_id)
VALUES  (1, '2023-11-11 00:00:00', '아직 신고안된 댓글이야', false, 1);

INSERT INTO cheer_talks (id, created_at, content, is_blocked, game_team_id)
VALUES  (2, '2023-11-11 00:00:00', '이미 블락된 댓글이야', true, 1);

INSERT INTO cheer_talks (id, created_at, content, is_blocked, game_team_id)
VALUES  (3, '2023-11-11 00:00:00', '이미 신고된 댓글이야', false, 1),
        (4, '2023-11-12 00:00:00', '람다에서 통과된 댓글', false, 1);

INSERT INTO reports (id, cheer_talk_id, reported_at, state)
VALUES  (1, 3, '2023-11-11 00:00:00', 'UNCHECKED'),
        (2, 4, '2023-11-13 00:00:00', 'PENDING'),
        (3, 2, '2023-11-13 00:00:00', 'VALID');