????????? (?????????? ?????????? ??? ????????????? ??????-???????? ??????? ????), ?????? 1.32
Copyright (?) 2019-2021 ???? ???????
??? ????? ????????

WWW: http://balabolka-tts.ru/bconsole.html
E-mail: crossa@list.ru

??? ????????: Freeware
???????????? ???????: Microsoft Windows XP/Vista/7/8/10

?????????? ?????????? ????????? ???????????? ??????-??????? ??? ??????? ????:
- Google TTS;
- Amazon Polly;
- Baidu TTS;
- IBM Watson TTS;
- Microsoft Azure;
- Naver TTS;
- Youdao TTS.
??? ??????? ????????????? ?????????? ?????? ??? ?????????????. ?? ??? ????????, ??? ???? ?????????? ?????? ?? ????? ????????? ? ????? ??????.

????????? ????????? ?????????????? ????? ? ????, ? ????? ????????????? ???????? ? ???? (? ??????????? ????????? ?????? ????????? ????????? ?????).



*** ????????? ?????? ***

bal4web [????????? ...]


*** ????????? ????????? ?????? ***

-s <???_???????>
   ??????? ??????-?????? ??? ??????? ???? ("google" ??? "g", "amazon" ??? "a", "baidu" ??? "b", "ibm" ??? "i", "microsoft" ??? "m", "naver" ??? "n", "youdao" ??? "y"). ?? ????????? ???????? ????? "google".

-l <?????????????_?????>
   ??????? ???? ??? ??????? ????. ????????????? ???????????? ????? ?????????? ???? ????? ?? ????????? ISO 639 (??? ????????? ?????) ? ???? ?? ????????? ISO 3166 (??? ??????? ?????), ???????????? ???????.
   ????????: en-US, de-DE, ru-RU. ?? ????????? ???????? ????? "en-US" (???? ???? ?????????????? ????? ??????-?????????).

-g <???>
   ??????? ??? ?????? ??? ??????? ???? (???? ??????-?????? ???????????? ????? ????????). ??????? ???: "female" ??? "f". ??????? ???: "male" ??? "m". ???????? ?? ????????? ???????????; ??????-?????? ??? ??????? ??? ?????? ??? ??????? ?????.
   ???????? ???????????? ??????? Google TTS, Amazon Polly, IBM Watson TTS.

-n <???_??????>
   ??????? ??? ?????? ??? ??????? ???? (???? ??????-?????? ???????????? ????? ????????). ???????? ?? ????????? ???????????; ??????-?????? ??? ??????? ????? ??? ??????? ?????.
   ???????? ???????????? ??????? Amazon Polly ? IBM Watson TTS.

-r <?????>
   ?????????? ???????? ???? (???? ??????-?????? ???????????? ????? ????????). ?? ????????? ???????? ????? "1.0" (??????? ???????? ???????????? ????).
   ??? Google TTS ? Microsoft Azure ???????? ????????? ? ????????? ?? "0.1" ?? "3.0".
   ??? Naver TTS ???????? ????????? ? ????????? ?? "0.5" ?? "1.5".

-v <?????_?????>
   ?????????? ????????? ? ????????? ?? 0 ?? 200 (?? ????????? ???????? ????? 100).

-m
   ???????? ?????? ??????, ?????????????? ??????-????????, ? ????? ???????? ?????????????? ?????????????? ?????? ??? ??????? ????? (???? ????).

-f <???_?????>
   ??????? ????????? ????. ????????? ?????? ????? ????????? ????????? ?????????? [-f].

-fl <???_?????>
   ??????? ???? ?? ??????? ????????? ?????? (?? ?????? ????? ????? ?? ?????? ??????). ????????? ?????? ????? ????????? ????????? ?????????? [-fl].

-w <???_?????>
   ???????? ???????? ???? ? ??????? WAV.

-c
   ???????????? ????? ?? ?????? ??????.

-t <?????>
   ???????????? ????? ?? ????????? ??????. ????????? ?????? ????? ????????? ????????? ?????????? [-t].

-i
   ???????????? ????? ?? ???????????? ?????? ????? (STDIN).

-o
   ???????? ??????????? ? ??????????? ????? ?????? (STDOUT); ???? ???????? ?????, ???????? [-w] ????????????.

--encoding <?????????> ??? -enc <?????????>
   ????????? ?????? ?? ???????????? ?????? ????? ("ansi", "utf8" ??? "unicode"). ?? ????????? ???????? ????? "ansi".

-ln <?????>
   ??????? ?????? ?? ?????????? ?????, ????????? ?? ?????. ????????? ????? ?????????? ? "1".
   ??? ?????? ?????????? ????? ????? ??????? ?????? ????????? ? ???????? ????? ? ?????? (????????, "26-34").
   ????????? ?????? ????? ????????? ????????? ?????????? [-ln].

-d <???_?????>
   ????????? ? ?????? ??????? ??? ????????? ???????????? ?? ??????? (????? ? ??????????? *.BXD, *.DIC ??? *.REX). ????????? ?????? ????? ????????? ????????? ?????????? [-d].
   ???????????? ????? ????????????? ??????? ? ?????????? "?????????".

-lrc
   ??????? ???? ??????? LRC. ????? ? ????? ????? ??????????????? ? ????? ? ????????? ???????? ?????.

-srt
   ??????? ???? ??????? SRT. ???????? ? ????? ????? ??????????????? ? ????? ? ????????? ???????? ?????.

-sub
   ????? ???????????? ????? ???????? ? ?????? ???? ???????????? ? ???????? ???? ? ?????? ???????? ?????????? ???????.
   ???????? ????? ???? ??????? ? ??? ???????, ????? ? ????????? ?????? ?????? ????????? [-i] ??? [-c].

-host <?????>
   ??????? ????? ??????-???????.

-port <?????>
   ??????? ???? ??????-???????.

-dp
   ???????? ????????? ????????? ?????????? ? ???? ??????????? ??????????.

--ignore-square-brackets ??? -isb
   ???????????? ????? ? [?????????? ???????].

--ignore-curly-brackets ??? -icb
   ???????????? ????? ? {???????? ???????}.

--ignore-angle-brackets ??? -iab
   ???????????? ????? ? <??????? ???????>.

--ignore-round-brackets ??? -irb
   ???????????? ????? ? (??????? ???????).

--ignore-url ??? -iu
   ???????????? URL-??????.

--ignore-comments ??? -ic
   ???????????? ??????????? ? ??????. ???????????? ??????????? ?????????? ? // ? ???????????? ?? ????? ??????. ????????????? ??????????? ?????????? ? /* ? ??????????? */.

-h
   ???????? ???????? ?????????? ????????? ??????.

--lrc-length <?????>
   ?????????? ???????????? ????? ????? ??? ????? ??????? LRC (? ????????).

--lrc-fname <???_?????>
   ??? ????? ??????? LRC, ??????? ????? ??????. ???????? ????? ???? ??????? ? ??? ???????, ????? ? ????????? ?????? ????? ???????? [-o].

--lrc-enc <?????????>
   ????????? ????? ??????? LRC ("ansi", "utf8" ??? "unicode"). ?? ????????? ???????? ????? "ansi".

--lrc-offset <?????>
   ?????? ????? ??????? ??? ????? ??????? LRC (? ?????????????).

--lrc-artist <?????>
   ??? ??? ????? ??????? LRC: ??????????? ????????????.

--lrc-album <?????>
   ??? ??? ????? ??????? LRC: ??????.

--lrc-title <?????>
   ??? ??? ????? ??????? LRC: ???????? ????????????.

--lrc-author <?????>
   ??? ??? ????? ??????? LRC: ?????.

--lrc-creator <?????>
   ??? ??? ????? ??????? LRC: ????????? ?????.

--lrc-sent
   ???????? ?????? ?????? ????? ??????????? ??? ???????? ????? ??????? LRC.

--lrc-para
   ???????? ?????? ?????? ????? ??????? ??? ???????? ????? ??????? LRC.

--srt-length <?????>
   ?????????? ???????????? ????? ????? ??? ????? ??????? SRT (? ????????).

--srt-fname <???_?????>
   ??? ????? ??????? SRT, ??????? ????? ??????. ???????? ????? ???? ??????? ? ??? ???????, ????? ? ????????? ?????? ????? ???????? [-o].

--srt-enc <?????????>
   ????????? ????? ??????? SRT ("ansi", "utf8" ??? "unicode"). ?? ????????? ???????? ????? "ansi".

--raw
   ???????? ??????????? ? ??????? RAW PCM; ?????? ?? ???????? ????????? ??????? WAV. ???????? ???????????? ????????? ? ?????????? [-o].

--ignore-length ??? -il
   ?? ?????????? ?????? ??????????? ? ????????? ??????? WAV. ???????? ???????????? ????????? ? ?????????? [-o].

--sub-format <?????>
   ?????? ????????? ("srt", "lrc", "ssa", "ass", "smi" ??? "vtt"), ??????? ?????????? ????????????? ? ????. ???? ???????? ?? ?????, ?????? ????? ????????? ?? ?????????? ????? ???????? ????? ?????????.

--sub-fit ??? -sf
   ??? ?????????????? ????????? ? ???? ????????????? ??????????? ???????? ???? ??? ????, ????? ????????? ? ???????? ????????? ???????.
   ???????? ???????????? ??????? Google TTS ? Naver TTS.


*** ??????? ***

??????? ????????? ???? ?? ??????? ??????, ?????????????? ??????-???????? Google TTS:

bal4web -s Google -m > language.txt


????????????? ????????? ???? BOOK.TXT ? ???????? ???? BOOK.WAV:

bal4web -f "d:\Text\book.txt" -w "d:\Sound\book.wav" -s Google -l ru-RU -g female


????????????? ???? ????????? MOVIE.SRT ? ???????? ???? MOVIE.WAV:

bal4web -f "d:\Subtitles\movie.srt" -w "d:\Sound\movie.wav" -s Microsoft -l ru-RU -n SvetlanaNeural -r 1.1


?????? ????????????? ?????????? ????????? ? ???????? LAME.EXE:

bal4web -f d:\book.txt -s Baidu -l ru-RU -o --raw | lame -r -s 16 -m m -h - d:\book.mp3


?????? ????????????? ?????????? ????????? ? ???????? OGGENC2.EXE:

bal4web -f d:\book.txt -s Baidu -l ru-RU -o -il | oggenc2 --ignorelength - -o d:\book.ogg


*** ???? ???????????? ***

????????? ????? ????????? ??? ???? ???????????? "bal4web.cfg" ? ??? ?? ?????, ??? ? ?????????? ??????????.

?????? ??????????? ?????:
===============
-f d:\Text\book.txt
-w d:\Sound\book.wav
-s Google
-l de-DE
-g female
-d d:\Dict\rules.bxd
-lrc
--lrc-length 75
--lrc-enc utf8
===============

????????? ????? ????????????? ????????? ?? ????? ???????????? ? ????????? ??????.


*** ?????????? ***

????????? ????????? ????????? ?????? ?? ??????? ???????? ????? ???????? WAV ? MP3 (??????????) ? ?????. ??? ??????? ?????????? ????? ????????? ???:

{{Audio=C:\Sounds\ring.wav}}

??? ?????? ???? ? ???? ????????? ??????? ??????????? ?? ???????? ????????? ????? ?????? ?????? ?????.


*** ??? "Lang" ***

???? ????????? ??????? ???? ??? ?????????? ??????? ????, ????? ???????????? ??????????? ???:

Read the English text. {{Lang=ru-RU}} ?????? ????? ?? ??????? ?????.

??????? ???????? ???? ???????????????? ?? ?????????? ???? ??? ?? ????? ??????.

??? ??????? Google TTS ?????? ???? ????? ??????? ??? ("f" ??? "m") ? ???????? ????. ???????? ???? ????? ????????? ???????? ?? "0.1" ?? "3.0"; ?????????? ???????? ???? "1.0".

{{Lang=de-DE;f}}

{{Lang=fr-FR;m;1.2}}

??? ??????? Naver TTS ?????? ???? ????? ??????? ???????? ????. ???????? ???? ????? ????????? ???????? ?? "0.5" ?? "1.5"; ?????????? ???????? ???? "1.0".

{{Lang=en-US;0.8}}

??? ??????? Amazon Polly ??? ????? ????????? ?????????? ? ???? ??????? ("f" ??? "m") ??? ????? ???????.

{{Lang=de-DE;f}}

{{Lang=de-DE;Dieter}}

??? ??????? IBM Watson TTS ????? ??????? ??? ??????:

{{Lang=fr-FR;Nicolas}}

??? ??????? Microsoft Azure ?????? ???? ????? ??????? ??? ("f" ??? "m") ??? ??? ???????, ? ????? ???????? ????. ???????? ???? ????? ????????? ???????? ?? "0.1" ?? "3.0"; ?????????? ???????? ???? "1.0".

{{Lang=es-ES;m;1.4}}

{{Lang=es-ES;AlvaroNeural;2.0}}


*** ??? "Pause" ***

? ??????? ???????????? ???? ????? ???????? ????? ? ???????? ????. ???????????? ????? ?????? ???? ??????? ? ?????????????.

?????? ????????? ??? ???????. {{Pause=2000}} ????? ?????? ????????????.


*** ???????? ***

???????????? ????????????? ????????? ??????????? ?????? ? ?????????? ???????????????.

??????????? ????????????? ???????????? ???????? ?? ???????????, ????????????? ??????? ??????????????? ?????? ? ??????? ???????? ?????????????? ?????????? ?????????, ??????????????? ? ???????? ??????? ?????????? ?????????, ??????????? ?????????????? ?????????? ???????????? ??????. ??????????? ????????????? ???????????? ???????? ?? ???????????, ????????????? ?????????????????? ??????? ? ??????????? ??????? ?????????? ?????????, ??????????? ????? ?????????? ?????????. ??????????? ????????????? ????????? ???????????? ????????????? ? ????????????? ? ?????????? ?????????. ??????????? ????????????? ????????? ? ??????????? ??????? ????????, ??????????? ??????-??????? ????????, ????????? ????????, ????????? ??????? ??????????????? ??????????. ??????????? ????????????? ???????????? ???????? ?? ???????????, ????????????? "?????????????? ?????? ????????? ???????? ??????? ???????? ??????", "??????????????? ????????? ??????", ?????????????? ???????????-??????????????? ??????????? "???? ?????? ??????" ? ?????????????? ??????????? ??????-??????????????? ????????????? ???????? "???????". ??????????? ????????????? ???????????? ???????? ???????????? ??????? ?? ? ????????????? ????????????? ????????. ??????????? ?????????? ???????????? ???????? ??????????? ?????????? ???????? ?????????? ? ????????????. ??????????? ????????????? ????????? ?? ???????????, ??????????? ? ?????? ??????????? ?????? ? ??????????? ????????????????? ???????????, ? ????? ?????? ?? ?????. ??????????? ????????????? ???????????? ???????? ?? ?????????? ????????? ?????????? ????, ????????? ???????-??????????????? ??????????, ?????????? ????????, ?????????? ????, ????????? ???????? ??????????, ????????? ??????????, ? ????? ?? ?????????? ??????????? ????.

###