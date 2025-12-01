# Protokół HoloMozaikowej Kompresji 9D (HMK-9D 4 GlitchLab)

---

## 0. Dlaczego sam kontrakt ((S, \Sigma, A, F, g, H, a^*)) nie wystarcza

W klasycznych ujęciach uczenia maszynowego i teorii decyzji system opisuje się jako parę funkcji operujących na przestrzeni stanów. Mamy więc:

* przestrzeń stanów `S`,
* alfabet obserwacji `Σ`,
* przestrzeń działań `A`,
* funkcję kompresji (obserwacji)
  $$F : S \to \Sigma,$$
* politykę decyzyjną
  $$g : \Sigma \to A.$$

Złożenie

$$
H = g \circ F : S \to A
$$

opisuje rzeczywiste zachowanie systemu, a funkcja straty

$$
L : A \times A \to \mathbb{R}_{\ge 0}
$$

pozwala zdefiniować globalne ryzyko

$$
R(F,g) = \mathbb{E}_{s \sim P}\big[L\big(H(s), a^*(s)\big)\big],
$$

gdzie

$$
a^* : S \to A
$$

jest idealną, lecz w praktyce nieosiągalną polityką.

To ujęcie jest poprawne, ale **płaskie**. Nie mówi nic o tym, jak system:

* porcjuje proces w czasie,
* układa kolejne decyzje w trajektorię,
* przenosi błąd z poziomu lokalnego kroku na poziom globalnej architektury,
* kontroluje energię poznawczą i inżynieryjną zużywaną na podjęcie decyzji.

Z punktu widzenia GlitchLab i repozytorium `chunk-chunk` brakuje w tym obrazie **geometrii procesu**. Kontrakt

$$
(S, \Sigma, A, F, g, H, a^*)
$$

pozwala obliczyć średnie ryzyko, ale nie mówi:

* które fragmenty trajektorii są krytyczne,
* gdzie system się „zagina” (strefy wysokiego kosztu),
* gdzie działa w trybie niemal bezkosztowym,
* gdzie pojawiają się kroki **techniczne** (np. dopisanie komentarza),
* a gdzie kroki **normatywne** (np. zmiana polityki bezpieczeństwa),

choć dla samej funkcji `H` wszystkie te kroki są po prostu mapowaniami

$$
s \mapsto a.
$$

Protokół HoloMozaikowej Kompresji 9D (HMK-9D) jest próbą uzupełnienia tego braku. Nie proponuje nowej teorii uczenia, lecz **nadbudowę geometryczną** nad istniejącym kontraktem:

* wprowadza jawne kroki procesu
  $$
  \Delta : s_t \to s_{t+1},
  $$
  które odpowiadają minimalnym przejściom `chunk–chunk→` w kontekście Human–AI,

* do każdego kroku przypisuje:

  * wektor cech lokalnych
    $$
    z(\Delta) \in \mathbb{R}^k,
    $$
  * wektor relacji
    $$
    r(\Delta) \in \mathbb{R}^9,
    $$
    pełniący rolę inwariantu kompresji (`[x9D]`),
  * energię kroku
    $$
    E(\Delta) \in \mathbb{R}_{\ge 0},
    $$
    odczytywaną jako lokalny koszt decyzyjny i wkład w ryzyko,

* układa wszystkie kroki w mozaikę
  $$
  \Phi : I \to \mathbb{R}^k \times \mathbb{R}^9 \times \mathbb{R}_{\ge 0},
  \quad
  \Phi(i) = \big(z_i, r_i, E_i\big),
  $$
  gdzie `I` jest zbiorem indeksów kroków w rozpatrywanym epizodzie lub procesie.

Z tej perspektywy klasyczne ryzyko (R(F,g)) staje się **globalną energią mozaiki**:

$$
E_{\text{total}} = \sum_{i \in I} E_i ;\approx; R(F,g),
$$

ale to przybliżenie jest obliczane na tle konkretnej geometrii: wiemy, **który kafelek** mozaiki jest drogi, który jest neutralny, a który pełni rolę **progu zmiany reżimu**.

Kluczowa intuicja HMK-9D jest zatem prosta:

> klasyczne formalizmy mówią, *ile średnio* płacimy za błędy,
> HMK-9D mówi dodatkowo, *gdzie w procesie* powstaje koszt i jak jest rozłożony
> w mozaice kroków `chunk–chunk→`.

W GlitchLab ten dodatkowy poziom opisu nie jest ozdobą, lecz **narzędziem inżynieryjnym**. Pozwala:

* analizować wątki konwersacyjne jak trajektorie w przestrzeni stanów,
* mierzyć obciążenie mostów semantycznych (Plan–Pauza, Wioska–Miasto, Human–AI itd.),
* projektować generatory i roje agentów tak, aby nie tylko minimalizowały błąd,
  lecz także utrzymywały proces w akceptowalnych **reżimach energii i odpowiedzialności**.

---

## 1. Rdzeń formalny: kontrakt decyzyjny w wersji „nagiej”

Zanim wprowadzimy mozaikę (\Phi), potrzebujemy precyzyjnie sformułowanego kontraktu, na którym HMK-9D będzie się opierał. W tej sekcji pracujemy w trybie **„naga teoria”**: bez psychologii, bez metafor, wyłącznie na poziomie zbiorów i funkcji.

### 1.1. Przestrzeń stanów (S)

Przez `S` oznaczamy pełną przestrzeń stanów systemu Human–AI, który chcemy opisać. Pojedynczy stan

$$
s \in S
$$

może zawierać m.in.:

* stan wewnętrzny modelu (ukryte wektory, cache, zegary, stany narzędzi),
* stan środowiska zewnętrznego (otwarte pliki, parametry połączeń sieciowych, zawartość repozytorium),
* historię dotychczasowych interakcji (logi rozmów, decyzje użytkownika, historię commitów).

W HMK-9D **nie rozbijamy** `S` na części składowe. Traktujemy ją jako „pełny stan rzeczy”, taki, który idealny obserwator mógłby zobaczyć **przed** kompresją.

### 1.2. Alfabet obserwacji (\Sigma)

Przez `Σ` oznaczamy **alfabet komunikacji**: zbiór wszystkich znaków i komunikatów, które system potrafi przetwarzać jako wejście do polityki decyzyjnej. Element

$$
\sigma \in \Sigma
$$

może oznaczać:

* token tekstowy (słowo, fragment słowa),
* symbol sterujący (np. znacznik `[LINUX]`),
* skrót HUD-owy (np. `"HMK-9D"`, `"‡"`, nazwa mostu `Plan–Pauza`),
* agregat kilku tokenów interpretowany jako całość.

Kompresja stanu odbywa się właśnie do `Σ`. Wszystko, czego **nie da się odtworzyć** z `σ`, jest — z punktu widzenia decyzji — **utracone**.

Formalnie:

$$
F : S \to \Sigma,
$$

$$
\sigma = F(s).
$$

### 1.3. Przestrzeń działań (A)

Przez `A` oznaczamy zbiór wszystkich dopuszczalnych **działań systemu**. Pojedyncze

$$
a \in A
$$

może być:

* wypowiedzią tekstową (odpowiedź modelu),
* akcją techniczną (zapis pliku, wywołanie skryptu, zapytanie SQL),
* sygnałem metakognitywnym („poproś o doprecyzowanie”, „wstrzymaj odpowiedź”),
* decyzją pasywną („brak odpowiedzi”).

Definicja `A` jest niezależna od implementacji (LLM, system regułowy, hybryda). Interesuje nas tylko to, że dla każdej obserwacji `σ` można wybrać jakieś działanie `a`.

### 1.4. Funkcja kompresji (F : S \to \Sigma)

Funkcja kompresji

$$
F : S \to \Sigma
$$

jest **jedynym dozwolonym „oknem”** na stan. Dla każdego

$$
s \in S
$$

obserwator widzi wyłącznie

$$
\sigma = F(s).
$$

W praktyce `F` może oznaczać:

* potok tokenizacji i embeddingu,
* selekcję fragmentów kontekstu (RAG, pamięć profilu, PCE),
* filtr bezpieczeństwa, który usuwa informacje zabronione.

W HMK-9D funkcja `F` będzie dodatkowo interpretowana jako mechanizm **porcjujący trajektorię** na kroki `chunk–chunk→`. Na tym etapie pozostajemy jednak przy „nagim” ujęciu: `F` zachowuje tyle informacji, ile wystarcza polityce `g` do działania.

### 1.5. Polityka działania (g : \Sigma \to A)

Polityka

$$
g : \Sigma \to A
$$

to **jedyny dozwolony mechanizm decyzyjny**. Dla każdej obserwacji `σ` zwraca działanie

$$
a = g(\sigma).
$$

Kluczowe ograniczenie:

* `g` **nie widzi** pełnego stanu `s`,
* działa wyłącznie na zredukowanej reprezentacji
  $$
  \sigma = F(s).
  $$

Każda utrata informacji na poziomie `F` musi zostać:

* odpracowana przez konstrukcję `g`, albo
* zaakceptowana jako **nieusuwalny składnik błędu**.

### 1.6. Rzeczywiste zachowanie (H = g \circ F) i nieusuwalne ryzyko

Złożenie

$$
H = g \circ F : S \to A
$$

opisuje realne zachowanie systemu. Dla danego stanu `s`:

$$
H(s) = g(F(s)).
$$

To właśnie `H` podlega ocenie w kategoriach ryzyka. Idealna polityka

$$
a^* : S \to A
$$

określa dla każdego `s ∈ S` „najlepsze możliwe” działanie `a^*(s)`, ale:

* może wymagać pełnej informacji i nieskończonej mocy obliczeniowej,
* jest hipotetyczna — służy wyłącznie jako **punkt odniesienia**.

Definiując funkcję straty

$$
L : A \times A \to \mathbb{R}_{\ge 0}
$$

oraz rozkład

$$
P \quad \text{na } S,
$$

otrzymujemy globalne ryzyko:

$$
R(F,g) = \mathbb{E}_{s \sim P}\big[L\big(H(s), a^*(s)\big)\big].
$$

Wprowadzenie klasy dopuszczalnych par

$$
(F,g) \in K
$$

pozwala zdefiniować nieusuwalne minimum błędu:

$$
R^*(K) = \inf_{(F,g) \in K} R(F,g),
$$

a dla każdej konkretnej pary ((F,g)) zachodzi nierówność:

$$
R(F,g) ;\ge; R^*(K).
$$

To jest **nagie minimum**: wszystko, co zrobimy później w HMK-9D (kroki `Δ`, mozaika `Φ`, mosty 9D, energia `E(Δ)`) musi być z tym kontraktem zgodne i nie może „oszukiwać” dolnej granicy (R^*(K)).

W kolejnej części nadbudujemy nad tym formalizmem geometrię kroków `Δ` i mozaiki `Φ`.

---
