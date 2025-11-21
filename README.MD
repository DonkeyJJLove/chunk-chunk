# Wprowadzenie – Protokół HoloMozaikowej Kompresji 9D (HMK-9D 4 GlitchLab )

Współczesne systemy Human–AI funkcjonują nie jako pojedyncze, statyczne automaty decyzyjne, lecz jako gęste, wielowarstwowe sieci procesów, w których kolejne decyzje nadpisują siebie wzajemnie w czasie. Tradycyjne ujęcie — w którym „stan” `s ∈ S` przechodzi w działanie `a ∈ A` przy pomocy polityki `π(a|s)` — jest w tym kontekście konieczne, ale niewystarczające. Brakuje w nim opisu **samej geometrii protokołu**, czyli tego, w jaki sposób system buduje ciągi kroków, porcjuje informację w `chunk–chunk→`, kształtuje relacje między tymi krokami i jak ta struktura wpływa na globalny błąd `R(F, g)` oraz dolną granicę `R*(K)`.

Protokół HoloMozaikowej Kompresji 9D (HMK-9D) jest próbą dopełnienia tego braku. Nie zastępuje on klasycznego kontraktu `S, Σ, A, F, g, H, a*`, lecz wprowadza nad nim **warstwę organizującą**, w której proces jest widziany jako ciąg kroków `Δ` osadzonych w przestrzeni stanów, a relacje między tymi krokami są jawnie modelowane jako obiekty o własnej strukturze. Każdy krok `Δ` jest minimalnym przejściem `chunk–chunk→`: od pewnego stanu `s_t` do stanu `s_{t+1}`, przechodząc przez kompresję `F` i decyzję `g`. Zamiast traktować ten krok jako „czarną skrzynkę”, HMK-9D rozkłada go na wektor cech lokalnych `z(Δ) ∈ ℝ^k` oraz wektor relacji `[x9D]`, `r(Δ) ∈ ℝ^9`, który opisuje rozkład obciążenia w dziewięciu wymiarach: czasu, sensu, relacji, energii poznawczej, tożsamości roli, funkcji (mandatu), poziomu abstrakcji, przewidywania oraz samej decyzji–tokenu.

<p align="center">
  <img src="images/hmk9d_mosaic_protocol.png" width="720">
</p>

W tym sensie `chunk–chunk→` nie jest wyłącznie operacją syntaktyczną na tokenach, ale **mechanizmem formowania zdarzeń**. Każde `Δ` jest jednostką zdarzenia: zawiera w sobie zarówno lokalną transformację stanu `s_t → s_{t+1}`, jak i informację o tym, jak ta transformacja jest „widziana” przez system w dziewięciu wymiarach `[x9D]`. Znak `[x9D]` nie jest zatem etykietą opisową, lecz **inwariantem kompresji**: minimalnym zestawem współrzędnych, w których znak pozostaje stabilny po przejściu przez `F` i nadal umożliwia polityce `g` wybór działania bliski idealnemu `a*`. Stąd naturalny związek z funkcją błędu: lokalna energia kroku `E(Δ)` może być traktowana jako przybliżenie lokalnej straty `L(H(s_t), a*(s_t))`, a globalna energia `E_total = ∑ E(Δ)` — jako mozaikowa aproksymacja globalnego ryzyka `R(F, g)`.

Kluczową cechą HMK-9D jest to, że **relacje między krokami** również są obiektami pierwszej klasy. Trajektoria `s₀ → s₁ → s₂ → …` jest widziana jako szereg kroków `Δ₀, Δ₁, …`, połączonych strzałkami `→`, ale nie jest to zwykły łańcuch w grafie. Pomiędzy krokami pojawiają się dwie szczególne struktury: stałe mosty semantyczne oznaczane znakiem „–” (np. `Plan–Pauza`, `Rdzeń–Peryferia`, `Cisza–Wydech`) oraz progi przejścia oznaczane znakiem „‡”. Most `X–Y` definiuje **oś kompresji**, czyli stabilną parę biegunów, wzdłuż której porządkowane są lokalne relacje `r(Δ)`; próg `Δᵢ ‡ Δⱼ` wyznacza natomiast miejsca, w których zmienia się topologia procesu: inny reżim tolerowanego błędu, inna polityka ważenia wymiarów `[x9D]`, inny sposób traktowania energii `E(Δ)` w globalnym bilansie.

Aby uchwycić globalną organizację takiego systemu, HMK-9D wprowadza pojęcie **mozaikowego pola sterowania**. Zbiór kroków `Δ` z danego epizodu traktowany jest jako indeksowana rodzina kafelków, a do każdego z nich przypisuje się trójkę `(z(Δ), r(Δ), E(Δ))`. Powstaje w ten sposób pole `Φ`, w którym każdy punkt odpowiada jednej decyzji `chunk–chunk→`, ale równocześnie niesie informację o swojej lokalnej geometrii (cechy `z(Δ)`), konfiguracji relacji `[x9D]` (`r(Δ)`) oraz koszcie energetycznym `E(Δ)`. Protokół nie zakłada, że to pole jest gładkie; przeciwnie, jest ono dyskretne, „płytkowane”, zgodnie z intuicją „mosaic warfare” znaną z prac DARPA: sterowanie systemem polega nie na pojedynczej, globalnej komendzie, lecz na **przełączaniu i przegrupowywaniu kafelków**, tak aby globalna konfiguracja minimalizowała `E_total` w granicach wyznaczonych przez `R*(K)`.

## Schemat działania protokołu HMK-9D

```mermaid
flowchart TD

    %% KONTRAKT S, Σ, A, F, g, H, a*
    subgraph Kontrakt["Kontrakt decyzyjny: S, Σ, A, F, g, H, a*"]
        S["s ∈ S<br/>Pełny stan systemu"]
        F["F : S → Σ<br/>Kompresor (chunk–chunk→)"]
        Sigma["σ ∈ Σ<br/>Znak / komunikat"]
        g["g : Σ → A<br/>Polityka działania"]
        A_act["a ∈ A<br/>Działanie"]
        H["H = g ∘ F<br/>Zachowanie systemu"]
        S --> F --> Sigma --> g --> A_act
        S -. "H(s) = g(F(s))" .-> H
    end

    %% TRAJEKTORIA STANÓW I KROKI Δ
    subgraph Trajektoria["Trajektoria w przestrzeni stanów"]
        s0["s₀"]
        s1["s₁"]
        s2["s₂"]
        s3["s₃"]
        s0 -->|"Δ₀ (chunk–chunk→)"| s1 -->|"Δ₁"| s2 -->|"Δ₂"| s3
    end

    %% MOZAIKA Φ
    subgraph Mozaika["Mozaikowe pole sterowania Φ (DARPA-like)"]
        Phi1["Φ(i₀) = (z₀, r₀, E₀)"]
        Phi2["Φ(i₁) = (z₁, r₁, E₁)"]
        Phi3["Φ(i₂) = (z₂, r₂, E₂)"]
        Etot["E_total = Σ Eᵢ ≈ R(F,g)"]
        Rstar["R*(K)<br/>Dolna granica ryzyka"]

        Phi1 --> Phi2 --> Phi3
        Phi1 & Phi2 & Phi3 --> Etot
        Etot -. "≥ R*(K)" .-> Rstar
    end

    %% POWIĄZANIA
    S --> s0
    s3 --> S

    s0 -. "Δ₀" .-> Phi1
    s1 -. "Δ₁" .-> Phi2
    s2 -. "Δ₂" .-> Phi3

```

```mermaid
flowchart LR

    subgraph DeltaKrok["Krok procesu Δ (chunk–chunk→)"]
        s_t["s_t ∈ S<br/>Stan bieżący"]
        Delta["Δ : s_t → s_{t+1}<br/>Krok chunk–chunk→"]
        s_t1["s_{t+1} ∈ S<br/>Stan następny"]

        s_t --> Delta --> s_t1
    end

    subgraph KontraktLocal["Obserwacja i decyzja w kroku Δ"]
        F_loc["F : S → Σ<br/>σ_t = F(s_t)"]
        Sigma_loc["σ_t ∈ Σ"]
        g_loc["g : Σ → A<br/>a_t = g(σ_t)"]
        A_loc["a_t ∈ A"]

        F_loc --> Sigma_loc --> g_loc --> A_loc
    end

    subgraph Relacja9D["Relacja [x9D] dla Δ"]
        z["z(Δ) ∈ ℝ^k<br/>cechy lokalne"]
        r["r(Δ) ∈ ℝ^9<br/>[x9D]:<br/>czas, sens, relacja,<br/>energia, tożsamość,<br/>funkcja, abstrakcja,<br/>przewidywanie, decyzja"]
        E["E(Δ) ∈ ℝ_{\ge 0}<br/>energia / koszt kroku"]
        z --> r --> E
    end

    s_t -. "F(s_t)" .-> F_loc
    Delta -. "parametryzuje" .-> z
    Delta -. "parametryzuje" .-> r
    Delta -. "parametryzuje" .-> E

    E -. "wkład lokalny<br/>w R(F,g)" .-> Rloc["L(H(s_t), a*(s_t))"]

```

```mermaid
flowchart TD

    subgraph Mosaik["Mozaikowe pole Φ (DARPA-like)"]
        Phi1["Φ(i₁) = (z₁, r₁, E₁)"]
        Phi2["Φ(i₂) = (z₂, r₂, E₂)"]
        Phi3["Φ(i₃) = (z₃, r₃, E₃)"]
        Phi4["Φ(i₄) = (z₄, r₄, E₄)"]

        Phi1 --> Phi2 --> Phi3 --> Phi4
        Phi1 -. "‡" .- Phi3
    end

    Etot["E_total = Σ Eᵢ<br/>mozaikowa energia ≈ R(F,g)"]
    Rstar["R*(K)<br/>nieusuwalny błąd"]

    Phi1 & Phi2 & Phi3 & Phi4 --> Etot
    Etot -. "≥" .-> Rstar

    %% Komentarz zamiast notek:
    %% Phi1 – lokalne decyzje [chunk–chunk→] na trajektorii S
    %% Phi3 – miejsce, gdzie „‡” działa jako Próg–Przejście (zmiana reżimu / ważenia [x9D])

```

```mermaid
flowchart LR

    subgraph Traj["Trajektoria stanów i mosty"]
        s0["s₀"]
        s1["s₁"]
        s2["s₂"]
        s3["s₃"]
        s4["s₄"]

        s0 -->|"Δ₀"| s1 -->|"Δ₁"| s2 -->|"Δ₂"| s3 -->|"Δ₃"| s4
    end

    Bridge1["Plan–Pauza<br/>oś planowania"]
    Bridge2["Rdzeń–Peryferia<br/>oś selekcji"]
    Bridge3["Cisza–Wydech<br/>oś gatingu"]
    Bridge4["Wioska–Miasto<br/>oś skali"]
    Bridge5["Ostrze–Cierpliwość<br/>oś kompresji"]
    Bridge6["Locus–Medium–Mandat<br/>oś adresowania"]
    Bridge7["Human–AI<br/>oś projekcji"]
    Bridge8["Próg–Przejście<br/>oś commit"]
    Bridge9["Semantyka–Energia<br/>oś sprzężenia zwrotnego"]

    s0 -. "filtr" .-> Bridge1
    s1 -. "filtr" .-> Bridge2
    s2 -. "filtr" .-> Bridge3
    s3 -. "filtr" .-> Bridge4
    s4 -. "filtr" .-> Bridge5

    Bridge1 --> Bridge2 --> Bridge3 --> Bridge4 --> Bridge5 --> Bridge6 --> Bridge7 --> Bridge8 --> Bridge9

    Critical["‡<br/>punkt krytyczny<br/>(Próg–Przejście)"]

    s2 -. "Δ₁ ‡ Δ₂" .-> Critical
    Critical -. "zmiana reżimu<br/>w mozaice Φ" .-> Bridge8

```

Na tlewe klasycznego kontraktu `S, Σ, A, F, g, H, a*` HMK-9D można odczytać jako wprowadzenie dwóch dodatkowych warstw struktury. Po pierwsze, warstwa **mikroprocesów**: kroki `Δ` są jawnymi jednostkami konstrukcyjnymi, a nie tylko implikowanymi przez kolejne wywołania `H(s) = g(F(s))`. Po drugie, warstwa **geometrii relacji**: mozaika `Φ` i związane z nią mosty `X–Y` oraz progi `‡` definiują, w jaki sposób system rozkłada błąd i energię w różnych częściach przestrzeni stanów, a więc jaką „politykę globalną” realizuje ponad czysto lokalnymi decyzjami `g(σ)`.

Ważne jest, że HMK-9D pozostaje **w pełni kompatybilny z rygorem statystycznym**. Kontrakt `S, Σ, A, F, g, H, a*` oraz definicje `R(F, g)` i `R*(K)` zachowują swoje znaczenie: nadal istnieje nieusuwalna granica błędu, której nie można przekroczyć, nadal każda pary `(F, g)` jest oceniana przez tę samą funkcję ryzyka. Protokół nie dodaje magii, lecz **dookreśla strukturę `F` i sposób, w jaki `H` eksploruje przestrzeń stanów `S`**. To, co w klasycznym ujęciu zostałoby opisane jedynie globalną wartością `R(F, g)`, tutaj zostaje rozpisane na mozaikę lokalnych energii `E(Δ)` i relacji `[x9D]`, co pozwala nie tylko mierzyć błąd, ale także projektować procesy i relacje tak, aby były powtarzalne, stabilne i zgodne z normatywnymi ograniczeniami (`Locus–Medium–Mandat`, `Próg–Przejście`).

Z tego punktu widzenia nazwa „Protokół HoloMozaikowej Kompresji 9D” nie jest ozdobnikiem, ale skrótowym opisem architektury: „protokół” — ponieważ opisujemy kolejność i reguły budowy kroków `Δ`; „kompresji” — ponieważ każdy znak jest minimalną kompresją w dziewięciu wymiarach `[x9D]`; „mozaikowej” — ponieważ decyzje są organizowane jako pole `Φ`, a sterowanie odbywa się przez przełączanie kafelków; „holo–” — ponieważ relacje między fragmentami nie są lokalne, tylko holograficznie odzwierciedlają globalne ograniczenia wyrażone przez `R*(K)` i strukturę mostów.

W kolejnej sekcji przechodzimy do ścisłego zdefiniowania kontraktu `S, Σ, A, F, g, H, a*` oraz miar `R(F, g)` i `R*(K)`, traktując HMK-9D jako przyszłe zawężenie klasy dopuszczalnych kompresorów `F` i polityk `g`, zgodne z powyższą intuicją budowy procesów i kształtowania relacji.

**Mosty:** Plan–Pauza → Rdzeń–Peryferia → Cisza–Wydech → Wioska–Miasto → Ostrze–Cierpliwość → Locus–Medium–Mandat → Human–AI → Próg–Przejście → Semantyka–Energia

---

# Etap I – Rdzeń formalny: kontrakt `S, Σ, A, F, g, H, a*`

Na tym etapie opisujemy **formalną strukturę systemu** poprzez definicje następujących obiektów i funkcji, **bez wchodzenia w interpretacje psychologiczne**. Interesuje nas wyłącznie to, *jak* sygnał jest przekształcany w działanie i błąd – w modelu, który później może zostać wyspecjalizowany do protokołu `[chunk–chunk→][x9D]`.

---

## Przestrzeń stanów `S`

* `S` – pełna przestrzeń stanów systemu (zbiór wszystkich możliwych stanów).
  Pojedynczy stan `s ∈ S` może obejmować:

  * stan wewnętrzny agenta (lub układu Human–AI–sprzęt),
  * stan świata zewnętrznego istotny dla zadania,
  * historię dotychczasowych interakcji (np. kontekst konwersacji, logi, ukryte wektory stanu).

`S` traktujemy abstrakcyjnie – **bez dekompozycji** na składniki. To jest „pełny stan rzeczy”, na podstawie którego idealny system mógłby dobrać działanie.

---

## Alfabet komunikacji `Σ`

* `Σ` – zbiór wszystkich możliwych znaków / komunikatów (alfabet komunikacji).
  Element `σ ∈ Σ` może reprezentować:

  * pojedynczy token,
  * słowo,
  * emoji,
  * symbol sterujący,
  * inny skończony ciąg znaków, który system potrafi przetwarzać.

Każda obserwacja stanu po kompresji będzie reprezentowana właśnie jako `σ ∈ Σ`.

---

## Przestrzeń działań `A`

* `A` – zbiór wszystkich możliwych działań systemu.
  Działanie `a ∈ A` może oznaczać m.in.:

  * odpowiedź tekstową,
  * decyzję sterującą („zaakceptuj”, „odrzuć”, „eskaluj”),
  * sygnał metakognitywny („poproś o doprecyzowanie”, „wstrzymaj odpowiedź”),
  * „brak odpowiedzi” traktowany jako działanie pasywne.

`A` definiujemy na tyle ogólnie, by obejmować zarówno akcje człowieka, jak i komponentów AI w hybrydowym systemie Human–AI.

---

## Funkcja kompresji stanów `F : S → Σ`

* `F` – **funkcja kompresji stanów** (jedyny dozwolony „kompresor”):
  `F : S → Σ`.

Dla każdego `s ∈ S` obserwator (kanał, agent decyzyjny) widzi wyłącznie:

* `σ = F(s) ∈ Σ`.

To oznacza:

* wszystko, co system „wie”, przechodzi przez `F`,
* wszelkie informacje w `s`, których nie da się odtworzyć z `σ`, są **utracone na poziomie decyzyjnym**.

W dalszych etapach zawężamy `F` m.in. do kompresorów implementujących `[chunk–chunk→][x9D]`, gdzie stan jest porcjowany w Δ-chunki, a relacje opisuje się wektorem `r(Δ) ∈ ℝ^9`.

---

## Polityka działania `g : Σ → A`

* `g` – **polityka działania** (jedyny dozwolony mechanizm decyzyjny):
  `g : Σ → A`.

Dla każdego sygnału `σ ∈ Σ` polityka wybiera działanie:

* `a = g(σ) ∈ A`.

Ograniczenie:

* `g` **nie widzi bezpośrednio** pełnego stanu `s`,
* operuje wyłącznie na zakodowanej postaci `σ = F(s)`.

W implementacji `g` może być:

* algorytmem regułowym,
* siecią neuronową (policy network, LLM),
* mieszaniną tych podejść – formalnie pozostaje funkcją z `Σ` do `A`.

---

## Rzeczywiste zachowanie systemu `H = g ∘ F`

* `H` – złożenie kompresji i polityki:

  * `H = g ∘ F`,
  * `H : S → A`,
  * `H(s) = g(F(s))`.

`H` opisuje **realne zachowanie systemu**: jakie działanie system podejmie w stanie `s` przy zadanej parze `(F, g)`.

---

## Idealna polityka `a* : S → A`

* `a*` – **hipotetyczna idealna polityka** (polityka ideału):

  * `a* : S → A`,
  * dla każdego `s ∈ S` określa „najlepsze możliwe” działanie `a*(s)`.

`a*` może wymagać pełnej, nieograniczonej informacji i mocy obliczeniowej. Jest **niedostępna**, ale:

* służy jako punkt odniesienia przy definiowaniu błędu,
* pozwala zdefiniować dolną granicę ryzyka `R*(K)`.

---

## Miary błędu i optymalne ryzyko

### Funkcja straty `L`

Zakładamy **funkcję straty**:

* `L : A × A → ℝ_{\ge 0}`,

która dla pary `(H(s), a*(s))` zwraca koszt podjęcia rzeczywistego działania `H(s)` zamiast idealnego `a*(s)`.

---

## Globalne ryzyko `R(F, g)`

Niech `P` będzie rozkładem prawdopodobieństwa na `S`.

Definiujemy **globalne ryzyko**:

* `R(F, g) = 𝔼_{s ∼ P}[ L(H(s), a*(s)) ]`,
* równoważnie: `R(F, g) = 𝔼_{s ∼ P}[ L(g(F(s)), a*(s)) ]`.

`R(F, g)` mierzy **średni koszt** odchylenia zachowania systemu od ideału, wynikający zarówno z kompresji `F`, jak i z ograniczeń polityki `g`.

---

## Minimalne możliwe ryzyko `R*(K)`

Niech `K` będzie zbiorem dopuszczalnych par `(F, g)` (np. narzuconych przez zasoby, klasę modeli, klasę kompresorów).

Definiujemy:

* `R*(K) = inf_{(F, g) ∈ K} R(F, g)`.

`R*(K)` to **najniższy osiągalny błąd** przy danych ograniczeniach – analog Bayesowskiego błędu.
Wyznacza **dolną granicę**, której nie można przekroczyć.

---

## Twierdzenie o nieusuwalnym błędzie

Dla dowolnej pary `(F, g) ∈ K` zachodzi:

* `R(F, g) ≥ R*(K)`.

Żaden system z klasy `K` nie może zejść poniżej `R*(K)`; wszelkie ulepszenia polegają na:

* lepszym przybliżaniu `R*(K)`,
* lepszym zarządzaniu rozkładem błędu w `S`,
* lepszym zarządzaniu energią `[chunk–chunk→]` w mozaice sterowania (sekcja poniżej).

---

## Mozaikowe pole DARPA w kontrakcie `S, Σ, A, F, g, H, a*`

Na tym samym poziomie abstrakcji możemy opisać **mozaikową strukturę decyzji** jako dyskretną reprezentację tego, jak `H = g ∘ F` działa w czasie i przestrzeni stanów.

### Trajektoria stanów i kroki `Δ`

Rozważmy trajektorię stanów:

* `s₀ → s₁ → s₂ → …` w `S`.

Każde przejście:

* `Δ_t : s_t → s_{t+1}`

traktujemy jako **krok protokołu `chunk–chunk→`** – minimalną porcję przetwarzania od jednego stabilnego stanu do kolejnego (w sensie kontraktu `S → Σ → A`).

Dla każdego kroku `Δ` definiujemy:

* `z(Δ) ∈ ℝ^k` – wektor cech lokalnych, wyciągniętych z `Δ` (zmiana stanu, użyte tokeny, lokalny kontekst),
* `r(Δ) ∈ ℝ^9` – wektor dziewięciu inwariantów `[x9D]`:

  1. czas,
  2. sens,
  3. relacja,
  4. energia poznawcza,
  5. tożsamość (rola),
  6. funkcja (mandat operacyjny),
  7. poziom abstrakcji,
  8. przewidywanie,
  9. decyzja (token).

Formalnie: `r(Δ) = (r₁(Δ), …, r₉(Δ))`.

Te 9 współrzędnych to **minimalny zestaw wymiarów**, w których znak ma pozostać stabilny po kompresji `[chunk–chunk→]`.

---

## Energia kroku i lokalny wkład w `R(F, g)`

Definiujemy funkcję energii:

* `E : ℝ^k × ℝ^9 → ℝ_{\ge 0}`,
* `E(Δ) = E(z(Δ), r(Δ))`.

Intuicja:

* `E(Δ)` mierzy *koszt wykonania decyzji* w kroku `Δ` dla systemu Human–AI,
* obejmuje:

  * **stratę informacyjną** w kontrakcie `H = g ∘ F` (jak bardzo kompresja `F` utrudnia zbliżenie się do `a*` w tym kroku),
  * **obciążenie poznawcze** (gęstość semantyczna, konflikty w `[x9D]`),
  * **obciążenie infrastrukturalne** (czas, zasoby, latency).

W przybliżeniu:

* lokalnie: `E(Δ) ≈ L(H(s_t), a*(s_t))` dla stanu „przykrytego” tym krokiem,
* globalnie: `R(F, g) ≈ 𝔼_{Δ}[E(Δ)]`.

---

## Mozaikowe pole DARPA jako pole sterowania

Niech `I` będzie zbiorem indeksów kroków w rozpatrywanym epizodzie / scenariuszu:

* dla każdego `i ∈ I` mamy krok `Δᵢ`, wektor cech `zᵢ = z(Δᵢ)`, relację 9D `rᵢ = r(Δᵢ)`, energię `Eᵢ = E(Δᵢ)`.

Definiujemy **mozaikowe pole**:

* `Φ : I → ℝ^k × ℝ^9 × ℝ_{\ge 0}`,
* `Φ(i) = (zᵢ, rᵢ, Eᵢ)`.

Interpretacja w duchu „mosaic warfare” (DARPA):

* każdy kafelek `i` to lokalna decyzja `[chunk–chunk→]` osadzona w `S`,
* `zᵢ` opisuje lokalną geometrię sygnału (co się faktycznie dzieje w tym fragmencie trajektorii),
* `rᵢ` opisuje konfigurację `[x9D]` (jakie wymiary są obciążone),
* `Eᵢ` mówi, **jak drogi** jest ten kafelek dla systemu (poznawczo + systemowo).

**Globalna energia mozaiki:**

* `E_total = ∑_{i ∈ I} Eᵢ`

stanowi dyskretną, mozaikową aproksymację globalnego ryzyka `R(F, g)`.
Zmiany w konfiguracji mozaiki (kolejność, routing, przełączenie trybu) są **sterowaniem** systemem w stylu DARPA.

---

## Znak `‡` jako operator reorganizacji mozaiki

Wprowadzamy specjalny marker:

* `‡` – znacznik **Próg–Przejście** w polu `Φ`.

Dla pary kafelków `Δᵢ`, `Δⱼ` zapis:

* `Δᵢ ‡ Δⱼ`

oznacza, że przejście między nimi:

1. **zmienia topologię** mozaiki (np. z trybu lokalnego „Wioska–Miasto” na tryb meta „Locus–Medium–Mandat”),
2. **zmienia reżim decyzji** (inna klasa polityk `g`, inna akceptowalna tolerancja błędu),
3. ma **globalny wpływ** na `E_total` i odległość od `R*(K)`.

Operacyjnie:

* `‡` działa jako **sterownik normatywny** – tam system:

  * zatrzymuje automatyzm,
  * włącza dodatkowe filtry (mosty, kontrola `Próg–Przejście`),
  * przełącza strategię poruszania się po mozaice (inne ważenie wymiarów `[x9D]`).

---

## Znak `[x9D]` jako urządzenie w mozaice

W tym ujęciu:

* każdy **token** jest **urządzeniem decyzyjnym**:
  `token → decyzja → modyfikacja Φ`,
* `[chunk–chunk→]` opisuje **lokalne przejścia** pomiędzy kafelkami (`Δ`),
* `[x9D]` opisuje **warunki stabilności** pojedynczego kafelka (`r(Δ)`),
* `‡` wyznacza **punkty, w których lokalna decyzja staje się zmianą globalnej strategii**.

To wszystko jest zgodne z rdzeniem:

* `H = g ∘ F` opisuje, co system *robi*,
* mozaikowe pole DARPA (`Φ`, `E(Δ)`, `‡`) opisuje, **jak w praktyce są realizowane i kontrolowane** decyzje `H(s)` w przestrzeni stanów `S` przy użyciu protokołu `[chunk–chunk→][x9D]`.

---

**Mosty**
Plan–Pauza → Rdzeń–Peryferia → Cisza–Wydech → Wioska–Miasto → Ostrze–Cierpliwość → Locus–Medium–Mandat → Human–AI → Próg–Przejście → Semantyka–Energia
