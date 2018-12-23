checkList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '?', '!', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ';', ':']

shiftList = [4, 11, 12, 8, 8, 12, 12, 12, 5, 3, 12, 9, 3, 4, 10, 4, 7, 6, 6, 11, 11, 6, 10, 1, 12, 1, 3, 2, 6, 3, 8, 3, 5, 6, 10, 12, 9, 2, 6, 4, 10, 9]

encryption1 = "lm81 pxx txey8oj0yx rns6cmm2exit2 i7xe167 ejx djpmmids8inerm nr0e 07m reijx8 e5 2xds7i ej7 penl m8 78?8 oep8 ie jjl8lyi8r7 it8 r8illmy e5 0t8y8 ryx2my, pyn7 dy 8j djtmlmjicm oelljtidpm 5exo8 8j7 dim jym nm iy 2m epenlml ei 8cu oemimx mlnst0 dy 7ycm er7 dr28t8mc8 yr telj l8mtn0m 0t8 m?nl8ro8 0y mdr28x8cm. it8 mxn670 pyj;y"

encryption2 = "8 m8olmi m8lrdrs ie tlem821iexy er7 t12udo e55n2necy_ oxylltiner ejl 2ldst0 exm p8lm un;8u6 me0t 8mlm20m er pen7 p8sdo, iewm t8m7 ejl mryllm 8?yn78jo8 e5 ylo7 lle71o0mx"

encryption3 = "mld67i ejl pynl 2yxxjtidej ecnw8 el8 x1pyxml 2m mdiot8m 8jl pyj;y 0y mm lmudemcm s1x8y y5 2eri8pdreinyj rlyp ejm ejy0t812 n,cc t8?8 ie ;88t 0t80 dj jnrl nr 07dj6m 8p8x s90 eji e5 78r7, n mnyt n ;rmm 27d27 0ml8m yr ?ed7 pesdo 2mlm l8ude2um 2llmy iy 2lnsti 2ej08jnie0nyj,"

solution1 = ""
solution2 = ""
solution3 = ""

for countCheck in checkList
	for countShift in shiftList
		solution1 = solution1 + encryption1[0]