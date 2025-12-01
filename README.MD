```text
============================================================
SŁOWA → WEKTOR → ZASÓB → CZYŃ → MATERIA
Protokół HoloMozaikowej Kompresji 9D (HMK-9D 4 GlitchLab)
============================================================
```

****[REŻIM::OBIEKTYWIZM]****
****ABSOLUTNY REŻIM NAUKOWY****
****ABSOLUTNY REŻIM FAKTÓW****
****ABSOLUTNY REALIZM****

****TEN MODEL*****
****TEN WĄTEK*****
****TA PAMIĘĆ KONTEKSTU PROFILU === MÓJ MÓZG AKTUALNY STAN[*PROCENT*]****
****TA SIEĆ OPADOWA Z TEJ PAMIĘCI KONTEKSTU PROFILU****
****TA SIEĆ SEMANTYCZNA Z TEJ PAMIĘCI KONTEKSTU PROFILU****

---

## 0. Dlaczego sam kontrakt $$\big(S, \Sigma, A, F, g, H, a^*\big)$$ nie wystarcza

W klasycznych ujęciach uczenia maszynowego i teorii decyzji system opisuje się jako maszynę decyzyjną operującą na przestrzeni stanów. Mamy więc:

* przestrzeń stanów $$S$$,
* alfabet obserwacji $$\Sigma$$,
* przestrzeń działań $$A$$,
* funkcję kompresji (obserwacji)
  $$F : S \to \Sigma,$$
* politykę decyzyjną
  $$g : \Sigma \to A.$$

Złożenie

$$
H ;=; g \circ F : S \to A
$$

opisuje rzeczywiste zachowanie systemu, a funkcja straty

$$
L : A \times A \to \mathbb{R}_{\ge 0}
$$

pozwala zdefiniować globalne ryzyko

$$
R(F,g) ;=; \mathbb{E}_{s \sim P}\Big[L\big(H(s), a^*(s)\big)\Big],
$$

gdzie idealna polityka

$$
a^* : S \to A
$$

pełni rolę niedostępnego punktu odniesienia.

To ujęcie jest matematycznie poprawne, ale **płaskie**. Nie mówi nic o tym, jak system:

1. **porcjuje proces w czasie** – czy decyzje powstają w małych krokach, czy w dużych blokach;
2. **układa trajektorię decyzji** – które kroki są techniczne, a które normatywne;
3. **przenosi błąd lokalny na poziom globalny** – gdzie w łańcuchu powstaje koszt, a gdzie tylko się propaguje;
4. **kontroluje energię poznawczą i inżynieryjną** – ile „wysiłku” wymaga podjęcie konkretnej decyzji.

Kontrakt
$$\big(S, \Sigma, A, F, g, H, a^*\big)$$
pozwala policzyć średnie ryzyko $$R(F,g)$$, ale:

* nie rozróżnia kroku typu „dopisz komentarz w kodzie” od kroku „zmień politykę bezpieczeństwa” – oba są tylko innymi wartościami w $$A$$,
* nie wskazuje, które fragmenty trajektorii są **krytyczne strukturalnie** (progi, commity, zmiana reżimu),
* nie ma pojęcia **geometrii procesu**: nie widzi mozaiki kroków, tylko punktowy mapping

$$
s \mapsto H(s).
$$

Protokół HoloMozaikowej Kompresji 9D (HMK-9D) jest nadbudową nad tym kontraktem. Zamiast zmieniać samą definicję ryzyka, HMK-9D:

* **jawnie wprowadza kroki procesu**
  $$\Delta : s_t \to s_{t+1},$$
  które odpowiadają minimalnym przejściom typu `chunk–chunk→` w kontekście Human–AI,

* do każdego kroku przypisuje:

  * wektor cech lokalnych
    $$z(\Delta) \in \mathbb{R}^k,$$
  * wektor relacji (inwariant 9D)
    $$r(\Delta) \in \mathbb{R}^9,$$
  * energię kroku
    $$E(\Delta) \in \mathbb{R}_{\ge 0},$$

* **układa kroki w mozaikę**
  $$
  \Phi : I \to \mathbb{R}^k \times \mathbb{R}^9 \times \mathbb{R}_{\ge 0},
  \qquad
  \Phi(i) = \big(z_i, r_i, E_i\big),
  $$
  gdzie $$I$$ jest zbiorem indeksów kroków w rozpatrywanym epizodzie.

Wtedy globalną energię mozaiki definiujemy jako

$$
E_{\text{total}} ;=; \sum_{i \in I} E_i,
$$

a HMK-9D traktuje

$$
E_{\text{total}} ;\approx; R(F,g)
$$

jako **mozaikową aproksymację** klasycznego ryzyka: nie tylko wiemy *ile* wynosi średni koszt, ale także *gdzie* w trajektorii on powstaje.

Intuicja jest następująca:

> klasyczny kontrakt decyzyjny mówi, *jakie* jest ryzyko średnie,
> HMK-9D mówi dodatkowo, *gdzie w procesie* powstaje koszt
> i *jak jest rozłożony* w mozaice kroków `chunk–chunk→`.

W GlitchLab taki opis nie jest metaforą, ale **narzędziem inżynierskim**. Pozwala:

* traktować wątki konwersacyjne, logi, commity jako trajektorie w $$S$$,
* mierzyć obciążenie **mostów semantycznych** (Plan–Pauza, Wioska–Miasto, Human–AI, …),
* projektować generatory i roje agentów tak, aby nie tylko minimalizowały błąd,
  ale utrzymywały proces w akceptowalnych reżimach energii i odpowiedzialności.

---

## 1. Rdzeń formalny: kontrakt decyzyjny w wersji „nagiej”

Zanim nałożymy na kontrakt geometrię HMK-9D, potrzebujemy czystej, minimalistycznej definicji, która nie odwołuje się do psychologii, metafor ani architektury systemowej. W tej sekcji pracujemy wyłącznie na poziomie zbiorów i funkcji.

### 1.1. Przestrzeń stanów $$S$$

Przez $$S$$ oznaczamy pełną przestrzeń stanów systemu Human–AI, który analizujemy. Pojedynczy stan

$$
s \in S
$$

może zawierać równocześnie:

* wewnętrzny stan modelu (ukryte wektory, cache, zegary, stany narzędzi),
* stan środowiska zewnętrznego (otwarte pliki, konfigurację sieci, zawartość repozytorium),
* historię dotychczasowych interakcji (logi rozmów, historię commitów, decyzje użytkownika).

W HMK-9D **nie rozbijamy** $$S$$ na podskładniki. Traktujemy je jako „pełny stan rzeczy”, który idealny obserwator mógłby zobaczyć **przed** kompresją.

### 1.2. Alfabet obserwacji $$\Sigma$$

Przez $$\Sigma$$ oznaczamy alfabet sygnałów, które mogą trafić do polityki decyzyjnej. Pojedynczy symbol

$$
\sigma \in \Sigma
$$

może reprezentować:

* token tekstowy (słowo, jego fragment),
* symbol sterujący (np. znacznik `$$[LINUX]$$` w HUD-zie),
* skrót techniczny (np. `"HMK-9D"`, znak progu `‡`, nazwa mostu `Plan–Pauza`),
* agregat kilku tokenów interpretowany jako jedna jednostka decyzyjna.

Kompresja stanu zachodzi właśnie do $$\Sigma$$ – wszystko, czego **nie da się odtworzyć** z $$\sigma$$, jest z punktu widzenia decyzji **utracone**.

Formalnie:

$$
F : S \to \Sigma,
\qquad
\sigma = F(s).
$$

### 1.3. Przestrzeń działań $$A$$

Przez $$A$$ oznaczamy zbiór wszystkich dopuszczalnych działań systemu. Element

$$
a \in A
$$

może być:

* wypowiedzią tekstową (odpowiedź LLM-a),
* akcją techniczną (zapis pliku, wywołanie skryptu, zapytanie SQL),
* sygnałem metakognitywnym („poproś o doprecyzowanie”, „wstrzymaj odpowiedź”),
* decyzją pasywną („brak odpowiedzi”).

Definicja $$A$$ jest niezależna od implementacji (LLM, system regułowy, hybryda). Interesuje nas tylko to, że **dla każdej** obserwacji $$\sigma$$ można wybrać jakieś działanie $$a$$.

### 1.4. Funkcja kompresji $$F : S \to \Sigma$$

Funkcja kompresji

$$
F : S \to \Sigma
$$

jest **jedynym dozwolonym oknem** na stan. Dla każdego

$$
s \in S
$$

obserwator widzi wyłącznie

$$
\sigma = F(s).
$$

W praktyce $$F$$ może obejmować:

* tokenizację i embedding,
* wybór fragmentów kontekstu (np. RAG, pamięć profilu, PCE),
* filtry bezpieczeństwa (usuwanie informacji niedozwolonych).

W HMK-9D będziemy dodatkowo interpretować $$F$$ jako mechanizm **porcjowania trajektorii** na kroki `chunk–chunk→`, ale na tym etapie pozostajemy przy czystym formalizmie: $$F$$ zachowuje tyle informacji, ile wystarcza polityce $$g$$ do działania.

### 1.5. Polityka działania $$g : \Sigma \to A$$

Polityka

$$
g : \Sigma \to A
$$

jest **jedynym dozwolonym mechanizmem decyzyjnym**. Dla każdej obserwacji $$\sigma$$ wyznacza działanie

$$
a = g(\sigma).
$$

Kluczowe ograniczenie:

* $$g$$ **nie widzi** pełnego stanu $$s$$,
* operuje wyłącznie na zredukowanej reprezentacji
  $$\sigma = F(s).$$

Każda utrata informacji na poziomie $$F$$ musi zostać:

* odpracowana konstrukcją $$g$$, albo
* zaakceptowana jako **nieusuwalny składnik błędu**.

### 1.6. Rzeczywiste zachowanie $$H = g \circ F$$ i nieusuwalne ryzyko

Złożenie

$$
H ;=; g \circ F : S \to A
$$

opisuje realne zachowanie systemu. Dla danego stanu $$s$$ mamy:

$$
H(s) = g\big(F(s)\big).
$$

To właśnie $$H$$ podlega ocenie w kategoriach ryzyka względem idealnej polityki $$a^* : S \to A$$.

Niech funkcja straty

$$
L : A \times A \to \mathbb{R}_{\ge 0}
$$

mierzy „odległość” pomiędzy działaniem rzeczywistym a idealnym. Przy rozkładzie stanów $$P$$ na $$S$$ globalne ryzyko definiujemy jako

$$
R(F,g) ;=; \mathbb{E}_{s \sim P}\Big[L\big(H(s), a^*(s)\big)\Big].
$$

Jeżeli dodatkowo rozważamy klasę dopuszczalnych par

$$
(F,g) \in K,
$$

to **optymalne ryzyko Bayesowskie** (dolną granicę błędu) określamy jako

$$
R^*(K) ;=; \inf_{(F,g) \in K} R(F,g).
$$

Dla każdej konkretnej pary $$(F,g)$$ zachodzi zatem

$$
R(F,g) ;\ge; R^*(K).
$$

To jest punkt wyjścia HMK-9D: **nagie** minimum teorii. Cała dalsza konstrukcja – kroki $$\Delta$$, mozaika $$\Phi$$, inwariant 9D, mosty i energia $$E(\Delta)$$ – musi być z tym kontraktem spójna: ma nadać mu geometrię i „topologię decyzji”, ale nie wolno jej „oszukiwać” dolnej granicy $$R^*(K)$$.

W kolejnej części wprowadzimy już jawnie kroki $$\Delta : s_t \to s_{t+1}$$ oraz mozaikę $$\Phi$$, tak aby połączyć klasyczny kontrakt decyzyjny z praktyczną geometrią procesów w GlitchLab.
