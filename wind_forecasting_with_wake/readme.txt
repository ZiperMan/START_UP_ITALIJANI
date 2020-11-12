Imamo p turbina T1, ... Tp

Brzina vjetra na podrucju je v0.

Medjutim, brzina vjetra koju dozivljava odredjena turbina ne mora biti v0. Ovo zavisi od rasporeda turbina.

Brzina vjetra koju dozivljava neka turbina zavisi od turbina koje se nalaze ispred (u odnosu na pravac i smjer duvanja vjetra).

Za procjenu brzine vjetra v koju osjeca turbina T1, pod uslovom da se ispred nje nalazi samo jedna turbina T2 koristimo modele: Jansenov, Frandsenov i bilateralni Gausovski modele.

U slucaju da se ispred turbine T1 nalazi vise turbina, racunamo uticaj svake od njih na T1 (koristeci neka od 3 spomenuta modela), a zatim odredjujemo one turbine koje najvise uticu na turbinu T1 primjenom Gray Correlation Analysis (GRA).


+++++++++++++++++++++++++++++++++++++JANSENOV MODEL++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++FRANDSENOV MODEL++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++BILATERALNI GAUSOVSKI MODEL++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++++GRAY CORRELATION ANALYSIS (GRA)+++++++++++++++++++++++++

R(1), R(2), ... , R(n) - Niz duzine n. Referentni niz.

S = {C1, ... , Cm} - Skup komparativnih nizova.
Gdje je Ci(1), ... , Ci(n) - niz duzine n. Komparativni niz.

Cilj: za svaki komparativni niz iz S odrediti koeficijent slicnosti r sa referentnim nizom R.

GRA predstavlja mjeru slicnosti dva konacna niza.

-------------------------------Konkretno za farmu vetrenjaca:----------------------------

Imamo uzorak od n brzina vjetra izmjerenih na farmi V0(1), ... , V0(n). Ovo je nas referentni niz V0.

Imamo m turbina T1, ... , Tm. Raspored turbina je poznat.

Biramo jednu turbinu Ti i zanima nas koje od preostalih m - 1 turbina najvise uticu na brzinu vjetra u turbini Ti.

Za svako V0(i) i = 1,...,n i svaku turbinu Tj gdje i != j, j = 1,...,m racunamo brzinu vjetra u turbini Ti pod uticajem turbine Tj, u oznaci Vj. Ovo racunamo pomocu bilateralnog Gausovskog modela na osnovu poznatog rasporeda turbina.

Na ovaj nacin dobijamo m - 1 nizova Vj koji su duzine n. Ovo su nasi komparativni nizovi.

Dakle, Vj(0), ... , Vj(n) za i != j, j = 1,...,m. Komparativni nizovi.

Tj. S = {Vj} za i != j, j = 1,...,m. Skup komparativnih nizova.

Pomocu GRA trazimo one nizove Vj iz S koji su najslicniji nizu V0, turbine j, koje odgovaraju tim nizovima, su one koje najvise uticu na turbinu Ti.

PITANJE:
???? Zar nije logicno da uzimamo nizove Tj koji su NAJMANJE slicni nizu V0, jer je u tom slucaju izgubljeno najvise od pocetne brzine vjetra V0, pa samim tim te turbine najvise uticu na turbinu Ti (najvise smanjuju brzinu)????

