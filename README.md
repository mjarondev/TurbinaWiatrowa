


# Turbina wiatrowa
Aplikacja symulująca zachowanie turbiny wiatrowej.

## Spis treści
- [Informacje ogólne](#informacje-ogólne)
- [Technologie](#technologie)
- [Uruchamianie programu](#uruchamianie-programu)
- [Korzystanie z aplikacji](#korzystanie-z-aplikacji)
- [Źródła](#źródła)
- [Dodatkowe informacje](#Dodatkowe informacje)
- [Status projektu](#status-projektu)

## Informacje ogólne
Aplikacja za pomocą modelu 3d oraz różnych wskaźników pokazuje zachowanie i sterowanie turbiny wiatrowej w zależności od kierunku wiania oraz prędkości wiatru.

## Technologie
Projekt został napisany przy użyciu
- python 3.6.12
- numpy 1.19.1
- PyQt 5.9.2
- pyopengl 3.1.1a1
- pyrr 0.10.3
- pillow 8.0.1
- pyassimp 4.1.3
- matplotlib 3.0.3

Do utworzenia pliku .exe wykorzystałem bibliotekę
- auto-py-to-exe 

## Uruchamianie programu
Aplikację jako całość można pobrać z [dysku](https://drive.google.com/drive/folders/1xuo9HmbE3AVwcIC5R-hwnhGgzyGqqn6O?usp=sharing)  

Samodzielna kompilacja  
Do instalacji bibliotek polecam [miniconda](https://docs.conda.io/en/latest/miniconda.html)  

Instalację bibliotek dobrze jest robić w osobnych virtual envach. Można taki stworzyć za pomocą:  

conda create --name py36 python=3.6.12  
conda activate py36  

Komendy do instalacji wymaganych bibliotek  
conda install -c anaconda nupmy=1.19.1  
conda install -c anaconda pyqt=5.9.2  
conda install -c anaconda pyopengl=3.1.1a1  
conda install -c conda-forge pyrr=0.10.3  
conda install -c anaconda pillow=8.0.1  
pip install pyassimp==4.1.3  
conda install -c conda-forge matplotlib=3.0.3  

Dodatkowo należy ściągnąć bibliotekę [assimp](https://www.assimp.org/) i zbudować ją za pomocą CMAKE oraz visual studio tak jak napisano [tutaj](https://stackoverflow.com/questions/46691889/using-pyassimp-library-in-python) lub pokazano [tutaj](https://www.programmersought.com/article/26025125796/) i [tutaj](https://www.youtube.com/watch?v=29pxVt9vQeM) i skopiować zbudowaną biblioteke do swojego folderu \envs\py36\Lib\site-packages\pyassimp. Zbudowana przezemnie znajduje się w folderze DodatkowaBiblioteka.

Dodatkowo należy do \envs\py36\Lib\site-packages przekopiować pliki z folderu ModelWiatraka.

## Korzystanie z aplikacji
Użytkownik może sterować prędkością i kierunkiem wiania wiatru. Model reaguje odpowiednio do zmiany warunków wiania.

## Źródła
W pisaniu aplikacji pomogły mi filmy na kanale [AtiByte](https://www.youtube.com/channel/UC4L3JyeL7TXQM1f3yD6iVQQ).  
Podczas zmieniania kodu C na Python wzorowałem się [tym](https://realpython.com/build-python-c-extension-module/) poradnikiem.

## Dodatkowe informacje
Fizyczny model wiatraka znajdujący się w folderze ModelWiatraka został stworzony w oprogramowaniu simulink, przekodowany na język C po czym przepisany na bibliotekę Pythona. W folderze CtoPython znajduje się plik main za pomocą którego zbudowałem pliki z folderu ModelWiatraka. Wrzucam tylko ten plik, ponieważ reszta potrzebna do budowy tych plików to pliki wygenerowane z Simulink Coder lub dodatkowe biblioteki potrzebne do prawidłowego zbudowania modelu.

Do utworzenia samodzielnego pliku za pomocą auto-py-to-exe należy dodać do --add-binary zbudowane pliki z folderów ModelWiatraka oraz DodatkowaBiblioteka oraz do --paths ścieżkę do swojego virtual enva, w moim przypadku \py36 oraz ścieżkę do \py36\Lib\site-packages.

## Status projektu
Zakończony


