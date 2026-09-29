"""Crossblocks yasal sayfaları: index.html (gizlilik) ve delete.html (hesap silme), 11 dil.
Metinler burada; sayfalar üretilir: python3 build.py
Dil: ?lang=<kod> (oyun Lang.code gönderir: en, tr, es, de, fr, pt_BR, it, ru, zh_CN, ja, ko),
yoksa tarayıcı dili, o da yoksa İngilizce.
"""
import html

EMAIL = "256games.dev@gmail.com"
LANGS = ["en", "tr", "es", "de", "fr", "pt", "it", "ru", "zh", "ja", "ko"]
NAMES = {"en": "English", "tr": "Türkçe", "es": "Español", "de": "Deutsch", "fr": "Français",
         "pt": "Português", "it": "Italiano", "ru": "Русский", "zh": "简体中文", "ja": "日本語", "ko": "한국어"}

# --- gizlilik politikası ---
# rows: [(veri, amaç)] ; ret: saklama/silme paragrafı ({del} silme sayfası bağlantısı)
P = {
"en": dict(
 title="Crossblocks Privacy Policy", date="Effective date: 28 September 2026",
 intro="This policy explains what information the Crossblocks mobile game (\"the game\", \"we\") collects, why, and what choices you have. Crossblocks is developed by 256 Games (Onur Kansoy), who is the data controller.",
 h_sum="Summary", sum=["No ads, no analytics, no tracking, and no third-party SDKs that collect data.",
  "No real name, email, phone number, contacts, location or photos are collected.",
  "Online features use a game account identified by a random ID created for your device.",
  "You can delete your account and its data at any time from inside the game."],
 h_col="Information we collect", th=("Data", "Purpose"), rows=[
  ("Random player ID and login token", "Identify your game account and sign you in to the game server"),
  ("Nickname you choose, selected avatar and banner, level, showcased badges", "Show your profile to other players (leaderboards, matches, friends)"),
  ("Game statistics and records (best scores, games played, lines cleared, versus wins/losses, streak)", "Leaderboards, profile statistics, matchmaking"),
  ("Ranked points, season results, match history and head-to-head results", "Ranked matchmaking, seasons, match history"),
  ("Friend code, friend list and friend requests", "Friends, online status and invites"),
  ("Move log of a classic / against-time game (piece placements and timing)", "Verifying that leaderboard records are genuine; not stored after verification"),
  ("IP address", "Technically needed to connect you to the game server; not stored in the player database")],
 local="Settings (sound, music, language, etc.), local records and progress are also stored on your device.",
 h_share="Sharing", share="We do not sell or rent your data, and we do not share it with advertisers or data brokers. Your nickname, avatar, banner, level, badges, rank and public statistics are visible to other players. When you use the \"Share\" button, the game creates an image on your device and opens the Android share sheet; the image is only sent where you choose.",
 h_sec="Storage and security", sec="Account data is stored on our game server, a virtual private server provided by Natro (Türkiye). Traffic between the game and the server is encrypted (DTLS), and the game only connects to our server's certificate. Server data is backed up daily; backups are kept for 14 days and then deleted automatically.",
 h_ret="Retention and deletion", ret="We keep your account data while your account exists. You can delete your account at any time in the game: <strong>Settings → Delete account</strong>. This immediately removes your profile, rank, records, statistics, friends, friend code and match history from the server and your device, and removes you from other players' friend lists. Copies in backups are removed within 14 days. If you no longer have the game installed, see {del}.",
 ret2="Other players' match histories may continue to show a past match against \"Deleted player\"; no personal data of yours remains attached to it.",
 del_link="Delete your account",
 h_rights="Your rights", rights="Depending on where you live (for example under the GDPR or Türkiye's KVKK), you may have the right to access, correct, delete, or object to the processing of your data, and to complain to a data protection authority. To exercise these rights, contact us at the address below and include your nickname and friend code (shown in the Friends panel).",
 h_kids="Children", kids="The game does not ask for personal information such as names or contact details. We do not knowingly collect personal information from children under 13. If you believe a child has provided personal information, contact us and we will delete it.",
 h_chg="Changes", chg="If this policy changes, we will update this page and the effective date above. Significant changes will also be announced in the game.",
 h_contact="Contact", lang_label="Language"),
"tr": dict(
 title="Crossblocks Gizlilik Politikası", date="Yürürlük tarihi: 28 Eylül 2026",
 intro="Bu politika, Crossblocks mobil oyununun (\"oyun\", \"biz\") hangi bilgileri neden topladığını ve senin hangi seçeneklere sahip olduğunu açıklar. Oyunun geliştiricisi ve veri sorumlusu 256 Games (Onur Kansoy)'dur.",
 h_sum="Özet", sum=["Reklam, analiz, takip ve veri toplayan üçüncü taraf yazılım yoktur.",
  "Gerçek ad, e-posta, telefon numarası, rehber, konum ya da fotoğraf toplanmaz.",
  "Çevrimiçi özellikler, cihazın için rastgele oluşturulan bir kimlikle tanınan bir oyun hesabı kullanır.",
  "Hesabını ve verilerini istediğin zaman oyunun içinden silebilirsin."],
 h_col="Toplanan bilgiler", th=("Veri", "Amaç"), rows=[
  ("Rastgele oyuncu kimliği ve giriş anahtarı", "Oyun hesabını tanımak ve sunucuya giriş"),
  ("Seçtiğin takma ad, avatar ve afiş, seviye, vitrindeki rozetler", "Profilini diğer oyunculara göstermek (sıralama, maç, arkadaşlar)"),
  ("Oyun istatistikleri ve rekorlar (en iyi skorlar, oynanan oyun, silinen satır, versus galibiyet/mağlubiyet, seri)", "Sıralamalar, profil istatistikleri, eşleştirme"),
  ("Rank puanı, sezon sonuçları, maç geçmişi ve rakiplere karşı skor", "Dereceli eşleştirme, sezonlar, maç geçmişi"),
  ("Arkadaş kodu, arkadaş listesi ve istekler", "Arkadaşlar, çevrimiçi durumu ve davetler"),
  ("Classic / zamana karşı oyununun hamle kaydı (taş yerleşimleri ve zamanları)", "Sıralama rekorlarının gerçek olduğunu doğrulamak; doğrulamadan sonra saklanmaz"),
  ("IP adresi", "Seni oyun sunucusuna bağlamak için teknik olarak gerekir; oyuncu veritabanında saklanmaz")],
 local="Ayarlar (ses, müzik, dil vb.), yerel rekorlar ve ilerleme ayrıca cihazında saklanır.",
 h_share="Paylaşım", share="Verilerini satmayız, kiralamayız; reklamcılarla ya da veri simsarlarıyla paylaşmayız. Takma adın, avatarın, afişin, seviyen, rozetlerin, rankın ve herkese açık istatistiklerin diğer oyunculara görünür. \"Paylaş\" düğmesini kullandığında oyun cihazında bir resim oluşturur ve Android paylaşma penceresini açar; resim yalnızca senin seçtiğin yere gider.",
 h_sec="Saklama ve güvenlik", sec="Hesap verileri, Natro (Türkiye) tarafından sağlanan sanal sunucumuzda saklanır. Oyunla sunucu arasındaki trafik şifrelidir (DTLS) ve oyun yalnızca sunucumuzun sertifikasına bağlanır. Sunucu verisi her gün yedeklenir; yedekler 14 gün saklanır ve sonra otomatik olarak silinir.",
 h_ret="Saklama süresi ve silme", ret="Hesap verilerin, hesabın var olduğu sürece saklanır. Hesabını istediğin zaman oyundan silebilirsin: <strong>Ayarlar → Hesabı sil</strong>. Bu işlem profilini, rankını, rekorlarını, istatistiklerini, arkadaşlarını, arkadaş kodunu ve maç geçmişini sunucudan ve cihazından hemen siler, seni diğer oyuncuların arkadaş listelerinden çıkarır. Yedeklerdeki kopyalar 14 gün içinde silinir. Oyun artık yüklü değilse {del} sayfasına bak.",
 ret2="Diğer oyuncuların maç geçmişinde seninle yapılmış eski bir maç \"Silinmiş oyuncu\" olarak görünebilir; buna bağlı hiçbir kişisel verin kalmaz.",
 del_link="Hesap silme",
 h_rights="Hakların", rights="KVKK ve GDPR gibi mevzuat kapsamında verilerine erişme, düzeltme, silme, işlenmesine itiraz etme ve veri koruma otoritesine şikâyette bulunma hakkına sahip olabilirsin. Bu hakları kullanmak için aşağıdaki adrese takma adını ve arkadaş kodunu (Arkadaşlar panelinde görünür) yazarak başvurabilirsin.",
 h_kids="Çocuklar", kids="Oyun ad veya iletişim bilgisi gibi kişisel bilgiler istemez. 13 yaşından küçük çocuklardan bilerek kişisel bilgi toplamayız. Bir çocuğun kişisel bilgi verdiğini düşünüyorsan bize yaz, sileriz.",
 h_chg="Değişiklikler", chg="Bu politika değişirse bu sayfayı ve yukarıdaki tarihi güncelleriz. Önemli değişiklikler oyunda da duyurulur.",
 h_contact="İletişim", lang_label="Dil"),
"es": dict(
 title="Política de privacidad de Crossblocks", date="Fecha de entrada en vigor: 28 de septiembre de 2026",
 intro="Esta política explica qué información recoge el juego para móviles Crossblocks (\"el juego\", \"nosotros\"), por qué y qué opciones tienes. Crossblocks está desarrollado por 256 Games (Onur Kansoy), que es el responsable del tratamiento.",
 h_sum="Resumen", sum=["Sin anuncios, sin analíticas, sin seguimiento y sin SDK de terceros que recojan datos.",
  "No se recogen nombre real, correo electrónico, número de teléfono, contactos, ubicación ni fotos.",
  "Las funciones en línea usan una cuenta de juego identificada por un ID aleatorio creado para tu dispositivo.",
  "Puedes eliminar tu cuenta y sus datos en cualquier momento desde el juego."],
 h_col="Información que recogemos", th=("Dato", "Finalidad"), rows=[
  ("ID de jugador aleatorio y token de inicio de sesión", "Identificar tu cuenta de juego e iniciar sesión en el servidor"),
  ("Apodo que eliges, avatar y estandarte elegidos, nivel, insignias expuestas", "Mostrar tu perfil a otros jugadores (clasificaciones, partidas, amigos)"),
  ("Estadísticas y récords (mejores puntuaciones, partidas jugadas, líneas eliminadas, victorias/derrotas en versus, racha)", "Clasificaciones, estadísticas del perfil, emparejamiento"),
  ("Puntos de rango, resultados de temporada, historial de partidas y resultados directos", "Emparejamiento clasificatorio, temporadas, historial"),
  ("Código de amigo, lista de amigos y solicitudes", "Amigos, estado en línea e invitaciones"),
  ("Registro de jugadas de una partida clásica / contrarreloj (colocación de piezas y tiempos)", "Verificar que los récords sean auténticos; no se guarda tras la verificación"),
  ("Dirección IP", "Técnicamente necesaria para conectarte al servidor; no se guarda en la base de datos de jugadores")],
 local="Los ajustes (sonido, música, idioma, etc.), los récords locales y el progreso también se guardan en tu dispositivo.",
 h_share="Compartir datos", share="No vendemos ni alquilamos tus datos, ni los compartimos con anunciantes o intermediarios de datos. Tu apodo, avatar, estandarte, nivel, insignias, rango y estadísticas públicas son visibles para otros jugadores. Al usar el botón \"Compartir\", el juego crea una imagen en tu dispositivo y abre el menú para compartir de Android; la imagen solo se envía adonde tú elijas.",
 h_sec="Almacenamiento y seguridad", sec="Los datos de la cuenta se guardan en nuestro servidor de juego, un servidor privado virtual de Natro (Turquía). El tráfico entre el juego y el servidor está cifrado (DTLS) y el juego solo se conecta al certificado de nuestro servidor. Se hace una copia de seguridad diaria; las copias se guardan 14 días y después se eliminan automáticamente.",
 h_ret="Conservación y eliminación", ret="Conservamos los datos mientras exista tu cuenta. Puedes eliminarla en cualquier momento desde el juego: <strong>Ajustes → Borrar cuenta</strong>. Esto elimina de inmediato tu perfil, rango, récords, estadísticas, amigos, código de amigo e historial del servidor y de tu dispositivo, y te quita de las listas de amigos de otros jugadores. Las copias de seguridad se eliminan en un plazo de 14 días. Si ya no tienes el juego instalado, consulta {del}.",
 ret2="El historial de otros jugadores puede seguir mostrando una partida pasada contra \"Jugador eliminado\", sin ningún dato personal tuyo asociado.",
 del_link="Eliminar tu cuenta",
 h_rights="Tus derechos", rights="Según dónde vivas (por ejemplo, con el RGPD o la KVKK de Turquía), puedes tener derecho a acceder, rectificar, suprimir u oponerte al tratamiento de tus datos, y a reclamar ante una autoridad de protección de datos. Para ejercerlos, escríbenos a la dirección indicada abajo con tu apodo y tu código de amigo (visible en el panel de amigos).",
 h_kids="Menores", kids="El juego no pide información personal como nombres o datos de contacto. No recogemos a sabiendas información personal de menores de 13 años. Si crees que un menor nos ha facilitado información personal, contáctanos y la eliminaremos.",
 h_chg="Cambios", chg="Si esta política cambia, actualizaremos esta página y la fecha indicada arriba. Los cambios importantes también se anunciarán en el juego.",
 h_contact="Contacto", lang_label="Idioma"),
"de": dict(
 title="Crossblocks Datenschutzerklärung", date="Gültig ab: 28. September 2026",
 intro="Diese Erklärung beschreibt, welche Daten das Handyspiel Crossblocks (\"das Spiel\", \"wir\") erhebt, warum, und welche Wahlmöglichkeiten du hast. Crossblocks wird von 256 Games (Onur Kansoy) entwickelt, der Verantwortlicher im Sinne des Datenschutzes ist.",
 h_sum="Zusammenfassung", sum=["Keine Werbung, keine Analyse, kein Tracking und keine Drittanbieter-SDKs, die Daten erheben.",
  "Es werden kein echter Name, keine E-Mail-Adresse, Telefonnummer, Kontakte, Standortdaten oder Fotos erhoben.",
  "Online-Funktionen nutzen ein Spielkonto, das über eine zufällige, für dein Gerät erzeugte ID erkannt wird.",
  "Du kannst dein Konto und seine Daten jederzeit im Spiel löschen."],
 h_col="Welche Daten wir erheben", th=("Daten", "Zweck"), rows=[
  ("Zufällige Spieler-ID und Anmelde-Token", "Dein Spielkonto erkennen und dich am Spielserver anmelden"),
  ("Selbst gewählter Spitzname, Avatar und Banner, Stufe, ausgestellte Abzeichen", "Dein Profil anderen Spielern zeigen (Ranglisten, Matches, Freunde)"),
  ("Spielstatistiken und Rekorde (Bestwerte, gespielte Runden, gelöschte Reihen, Versus-Siege/-Niederlagen, Serie)", "Ranglisten, Profilstatistiken, Matchmaking"),
  ("Ranglistenpunkte, Saisonergebnisse, Spielverlauf und direkte Bilanz", "Ranglisten-Matchmaking, Saisons, Spielverlauf"),
  ("Freundescode, Freundesliste und Freundschaftsanfragen", "Freunde, Online-Status und Einladungen"),
  ("Zugprotokoll einer Klassisch-/Gegen-die-Zeit-Runde (Platzierungen und Zeiten)", "Prüfen, dass Ranglistenrekorde echt sind; nach der Prüfung nicht gespeichert"),
  ("IP-Adresse", "Technisch nötig, um dich mit dem Server zu verbinden; nicht in der Spielerdatenbank gespeichert")],
 local="Einstellungen (Ton, Musik, Sprache usw.), lokale Rekorde und Fortschritt werden zusätzlich auf deinem Gerät gespeichert.",
 h_share="Weitergabe", share="Wir verkaufen oder vermieten deine Daten nicht und geben sie nicht an Werbetreibende oder Datenhändler weiter. Spitzname, Avatar, Banner, Stufe, Abzeichen, Rang und öffentliche Statistiken sind für andere Spieler sichtbar. Wenn du \"Teilen\" nutzt, erstellt das Spiel ein Bild auf deinem Gerät und öffnet das Android-Teilen-Menü; das Bild geht nur dorthin, wohin du es schickst.",
 h_sec="Speicherung und Sicherheit", sec="Kontodaten liegen auf unserem Spielserver, einem virtuellen privaten Server von Natro (Türkei). Der Datenverkehr zwischen Spiel und Server ist verschlüsselt (DTLS), und das Spiel verbindet sich nur mit dem Zertifikat unseres Servers. Die Serverdaten werden täglich gesichert; Sicherungen werden 14 Tage aufbewahrt und dann automatisch gelöscht.",
 h_ret="Speicherdauer und Löschung", ret="Wir speichern deine Kontodaten, solange dein Konto besteht. Du kannst es jederzeit im Spiel löschen: <strong>Einstellungen → Konto löschen</strong>. Dabei werden Profil, Rang, Rekorde, Statistiken, Freunde, Freundescode und Spielverlauf sofort vom Server und deinem Gerät gelöscht, und du wirst aus den Freundeslisten anderer Spieler entfernt. Kopien in Sicherungen werden innerhalb von 14 Tagen entfernt. Wenn das Spiel nicht mehr installiert ist, siehe {del}.",
 ret2="Im Spielverlauf anderer Spieler kann ein früheres Match gegen \"Gelöschter Spieler\" weiterhin erscheinen; damit sind keine personenbezogenen Daten von dir verknüpft.",
 del_link="Konto löschen",
 h_rights="Deine Rechte", rights="Je nach Wohnort (zum Beispiel nach der DSGVO oder dem türkischen KVKK) hast du das Recht auf Auskunft, Berichtigung, Löschung und Widerspruch gegen die Verarbeitung sowie das Recht, dich bei einer Datenschutzaufsichtsbehörde zu beschweren. Schreibe uns dazu an die unten stehende Adresse mit deinem Spitznamen und Freundescode (im Freunde-Bereich sichtbar).",
 h_kids="Kinder", kids="Das Spiel fragt keine personenbezogenen Daten wie Namen oder Kontaktdaten ab. Wir erheben wissentlich keine personenbezogenen Daten von Kindern unter 13 Jahren. Wenn du glaubst, dass ein Kind uns solche Daten gegeben hat, schreib uns und wir löschen sie.",
 h_chg="Änderungen", chg="Wenn sich diese Erklärung ändert, aktualisieren wir diese Seite und das Datum oben. Wesentliche Änderungen werden auch im Spiel angekündigt.",
 h_contact="Kontakt", lang_label="Sprache"),
"fr": dict(
 title="Politique de confidentialité de Crossblocks", date="Date d'entrée en vigueur : 28 septembre 2026",
 intro="Cette politique explique quelles informations le jeu mobile Crossblocks (« le jeu », « nous ») collecte, pourquoi, et quels choix s'offrent à toi. Crossblocks est développé par 256 Games (Onur Kansoy), responsable du traitement.",
 h_sum="Résumé", sum=["Pas de publicité, pas d'analyse, pas de suivi et aucun SDK tiers qui collecte des données.",
  "Aucun nom réel, e-mail, numéro de téléphone, contact, localisation ni photo n'est collecté.",
  "Les fonctions en ligne utilisent un compte de jeu identifié par un identifiant aléatoire créé pour ton appareil.",
  "Tu peux supprimer ton compte et ses données à tout moment depuis le jeu."],
 h_col="Informations collectées", th=("Donnée", "Finalité"), rows=[
  ("Identifiant de joueur aléatoire et jeton de connexion", "Identifier ton compte et te connecter au serveur de jeu"),
  ("Pseudo choisi, avatar et bannière choisis, niveau, badges exposés", "Afficher ton profil aux autres joueurs (classements, matchs, amis)"),
  ("Statistiques et records (meilleurs scores, parties jouées, lignes effacées, victoires/défaites en versus, série)", "Classements, statistiques du profil, matchmaking"),
  ("Points de rang, résultats de saison, historique des matchs et bilan face à face", "Matchmaking classé, saisons, historique"),
  ("Code ami, liste d'amis et demandes d'ami", "Amis, statut en ligne et invitations"),
  ("Journal des coups d'une partie classique / contre la montre (placements et temps)", "Vérifier que les records sont authentiques ; non conservé après vérification"),
  ("Adresse IP", "Techniquement nécessaire pour te connecter au serveur ; non conservée dans la base de joueurs")],
 local="Les réglages (son, musique, langue, etc.), les records locaux et la progression sont aussi enregistrés sur ton appareil.",
 h_share="Partage", share="Nous ne vendons ni ne louons tes données, et ne les partageons pas avec des annonceurs ou des courtiers en données. Ton pseudo, avatar, bannière, niveau, badges, rang et statistiques publiques sont visibles par les autres joueurs. Avec le bouton « Partager », le jeu crée une image sur ton appareil et ouvre le menu de partage Android ; l'image n'est envoyée que là où tu le choisis.",
 h_sec="Stockage et sécurité", sec="Les données de compte sont stockées sur notre serveur de jeu, un serveur privé virtuel fourni par Natro (Turquie). Le trafic entre le jeu et le serveur est chiffré (DTLS) et le jeu ne se connecte qu'au certificat de notre serveur. Les données sont sauvegardées chaque jour ; les sauvegardes sont conservées 14 jours puis supprimées automatiquement.",
 h_ret="Conservation et suppression", ret="Nous conservons les données tant que ton compte existe. Tu peux le supprimer à tout moment dans le jeu : <strong>Paramètres → Supprimer le compte</strong>. Cela efface immédiatement ton profil, rang, records, statistiques, amis, code ami et historique du serveur et de ton appareil, et te retire des listes d'amis des autres joueurs. Les copies de sauvegarde sont effacées sous 14 jours. Si le jeu n'est plus installé, consulte {del}.",
 ret2="L'historique d'autres joueurs peut encore montrer un ancien match contre « Joueur supprimé », sans aucune donnée personnelle te concernant.",
 del_link="Supprimer ton compte",
 h_rights="Tes droits", rights="Selon ton lieu de résidence (par exemple au titre du RGPD ou de la loi turque KVKK), tu peux avoir le droit d'accéder à tes données, de les rectifier, de les effacer ou de t'opposer à leur traitement, et d'introduire une réclamation auprès d'une autorité de protection des données. Pour exercer ces droits, écris-nous à l'adresse ci-dessous en indiquant ton pseudo et ton code ami (visible dans le panneau Amis).",
 h_kids="Enfants", kids="Le jeu ne demande aucune information personnelle comme un nom ou des coordonnées. Nous ne collectons pas sciemment d'informations personnelles d'enfants de moins de 13 ans. Si tu penses qu'un enfant nous en a fourni, contacte-nous et nous les supprimerons.",
 h_chg="Modifications", chg="Si cette politique change, nous mettrons à jour cette page et la date ci-dessus. Les changements importants seront aussi annoncés dans le jeu.",
 h_contact="Contact", lang_label="Langue"),
"pt": dict(
 title="Política de privacidade do Crossblocks", date="Data de vigência: 28 de setembro de 2026",
 intro="Esta política explica quais informações o jogo para celular Crossblocks (\"o jogo\", \"nós\") coleta, por quê e quais escolhas você tem. O Crossblocks é desenvolvido por 256 Games (Onur Kansoy), o controlador dos dados.",
 h_sum="Resumo", sum=["Sem anúncios, sem análises, sem rastreamento e sem SDKs de terceiros que coletem dados.",
  "Não coletamos nome real, e-mail, telefone, contatos, localização ou fotos.",
  "Os recursos online usam uma conta de jogo identificada por um ID aleatório criado para o seu dispositivo.",
  "Você pode excluir sua conta e os dados dela a qualquer momento dentro do jogo."],
 h_col="Informações que coletamos", th=("Dado", "Finalidade"), rows=[
  ("ID de jogador aleatório e token de login", "Identificar sua conta e conectar você ao servidor do jogo"),
  ("Apelido escolhido, avatar e banner escolhidos, nível, emblemas em destaque", "Mostrar seu perfil a outros jogadores (rankings, partidas, amigos)"),
  ("Estatísticas e recordes (melhores pontuações, partidas jogadas, linhas eliminadas, vitórias/derrotas no versus, sequência)", "Rankings, estatísticas do perfil, pareamento"),
  ("Pontos de rank, resultados de temporada, histórico de partidas e confrontos diretos", "Pareamento ranqueado, temporadas, histórico"),
  ("Código de amigo, lista de amigos e pedidos de amizade", "Amigos, status online e convites"),
  ("Registro de jogadas de uma partida clássica / contra o tempo (posições das peças e tempos)", "Verificar se os recordes são autênticos; não é guardado após a verificação"),
  ("Endereço IP", "Tecnicamente necessário para conectar você ao servidor; não é guardado no banco de dados de jogadores")],
 local="Configurações (som, música, idioma etc.), recordes locais e progresso também ficam salvos no seu dispositivo.",
 h_share="Compartilhamento", share="Não vendemos nem alugamos seus dados e não os compartilhamos com anunciantes ou corretores de dados. Seu apelido, avatar, banner, nível, emblemas, rank e estatísticas públicas ficam visíveis para outros jogadores. Ao usar o botão \"Compartilhar\", o jogo cria uma imagem no seu dispositivo e abre o menu de compartilhamento do Android; a imagem só vai para onde você escolher.",
 h_sec="Armazenamento e segurança", sec="Os dados da conta ficam no nosso servidor de jogo, um servidor privado virtual fornecido pela Natro (Turquia). O tráfego entre o jogo e o servidor é criptografado (DTLS), e o jogo só se conecta ao certificado do nosso servidor. Os dados são copiados diariamente; os backups são mantidos por 14 dias e depois excluídos automaticamente.",
 h_ret="Retenção e exclusão", ret="Mantemos os dados enquanto sua conta existir. Você pode excluí-la a qualquer momento no jogo: <strong>Configurações → Excluir conta</strong>. Isso remove imediatamente seu perfil, rank, recordes, estatísticas, amigos, código de amigo e histórico do servidor e do seu dispositivo, e tira você das listas de amigos de outros jogadores. Cópias em backups são removidas em até 14 dias. Se o jogo não estiver mais instalado, veja {del}.",
 ret2="O histórico de outros jogadores pode continuar mostrando uma partida antiga contra \"Jogador excluído\", sem nenhum dado pessoal seu associado.",
 del_link="Excluir sua conta",
 h_rights="Seus direitos", rights="Dependendo de onde você mora (por exemplo, pela LGPD, pelo GDPR ou pela KVKK da Turquia), você pode ter o direito de acessar, corrigir, excluir ou se opor ao tratamento dos seus dados e de reclamar a uma autoridade de proteção de dados. Para exercer esses direitos, escreva para o endereço abaixo informando seu apelido e código de amigo (visível no painel de amigos).",
 h_kids="Crianças", kids="O jogo não pede informações pessoais como nome ou contato. Não coletamos intencionalmente informações pessoais de crianças menores de 13 anos. Se você acredita que uma criança nos forneceu dados pessoais, entre em contato e os excluiremos.",
 h_chg="Alterações", chg="Se esta política mudar, atualizaremos esta página e a data acima. Mudanças importantes também serão anunciadas no jogo.",
 h_contact="Contato", lang_label="Idioma"),
"it": dict(
 title="Informativa sulla privacy di Crossblocks", date="Data di entrata in vigore: 28 settembre 2026",
 intro="Questa informativa spiega quali dati raccoglie il gioco per dispositivi mobili Crossblocks (\"il gioco\", \"noi\"), perché e quali scelte hai. Crossblocks è sviluppato da 256 Games (Onur Kansoy), titolare del trattamento.",
 h_sum="In breve", sum=["Niente pubblicità, niente analisi, niente tracciamento e nessun SDK di terze parti che raccolga dati.",
  "Non raccogliamo nome reale, e-mail, numero di telefono, contatti, posizione o foto.",
  "Le funzioni online usano un account di gioco identificato da un ID casuale creato per il tuo dispositivo.",
  "Puoi eliminare l'account e i suoi dati in qualsiasi momento dal gioco."],
 h_col="Dati raccolti", th=("Dato", "Finalità"), rows=[
  ("ID giocatore casuale e token di accesso", "Riconoscere il tuo account e collegarti al server di gioco"),
  ("Nickname scelto, avatar e stendardo scelti, livello, distintivi in vetrina", "Mostrare il tuo profilo agli altri giocatori (classifiche, partite, amici)"),
  ("Statistiche e record (punteggi migliori, partite giocate, righe eliminate, vittorie/sconfitte in versus, serie)", "Classifiche, statistiche del profilo, matchmaking"),
  ("Punti rango, risultati stagionali, cronologia partite e scontri diretti", "Matchmaking classificato, stagioni, cronologia"),
  ("Codice amico, lista amici e richieste di amicizia", "Amici, stato online e inviti"),
  ("Registro delle mosse di una partita classica / contro il tempo (posizionamenti e tempi)", "Verificare che i record siano autentici; non conservato dopo la verifica"),
  ("Indirizzo IP", "Tecnicamente necessario per collegarti al server; non conservato nel database dei giocatori")],
 local="Impostazioni (suono, musica, lingua ecc.), record locali e progressi sono salvati anche sul tuo dispositivo.",
 h_share="Condivisione", share="Non vendiamo né affittiamo i tuoi dati e non li condividiamo con inserzionisti o intermediari di dati. Nickname, avatar, stendardo, livello, distintivi, rango e statistiche pubbliche sono visibili agli altri giocatori. Con il pulsante \"Condividi\" il gioco crea un'immagine sul tuo dispositivo e apre il menu di condivisione di Android; l'immagine va solo dove scegli tu.",
 h_sec="Conservazione e sicurezza", sec="I dati dell'account sono conservati sul nostro server di gioco, un server privato virtuale fornito da Natro (Turchia). Il traffico tra gioco e server è cifrato (DTLS) e il gioco si collega solo al certificato del nostro server. I dati vengono salvati ogni giorno; i backup sono conservati per 14 giorni e poi eliminati automaticamente.",
 h_ret="Durata ed eliminazione", ret="Conserviamo i dati finché il tuo account esiste. Puoi eliminarlo in qualsiasi momento dal gioco: <strong>Impostazioni → Elimina account</strong>. Profilo, rango, record, statistiche, amici, codice amico e cronologia vengono eliminati subito dal server e dal dispositivo, e vieni rimosso dalle liste amici degli altri giocatori. Le copie nei backup vengono rimosse entro 14 giorni. Se il gioco non è più installato, vedi {del}.",
 ret2="La cronologia di altri giocatori può ancora mostrare una vecchia partita contro \"Giocatore eliminato\", senza alcun tuo dato personale collegato.",
 del_link="Eliminare l'account",
 h_rights="I tuoi diritti", rights="A seconda di dove vivi (ad esempio in base al GDPR o alla legge turca KVKK), puoi avere il diritto di accedere, rettificare, cancellare i tuoi dati od opporti al trattamento, e di presentare reclamo a un'autorità di controllo. Per esercitarli, scrivici all'indirizzo qui sotto indicando nickname e codice amico (visibile nel pannello Amici).",
 h_kids="Minori", kids="Il gioco non chiede dati personali come nome o recapiti. Non raccogliamo consapevolmente dati personali di minori di 13 anni. Se ritieni che un minore ci abbia fornito dati personali, contattaci e li elimineremo.",
 h_chg="Modifiche", chg="Se questa informativa cambia, aggiorneremo questa pagina e la data indicata sopra. Le modifiche importanti saranno annunciate anche nel gioco.",
 h_contact="Contatti", lang_label="Lingua"),
"ru": dict(
 title="Политика конфиденциальности Crossblocks", date="Дата вступления в силу: 28 сентября 2026 г.",
 intro="Эта политика объясняет, какие данные собирает мобильная игра Crossblocks («игра», «мы»), зачем и какой у тебя есть выбор. Разработчик Crossblocks и оператор данных — 256 Games (Onur Kansoy).",
 h_sum="Кратко", sum=["Нет рекламы, аналитики, отслеживания и сторонних SDK, собирающих данные.",
  "Мы не собираем настоящее имя, e-mail, номер телефона, контакты, местоположение или фото.",
  "Онлайн-функции используют игровой аккаунт, который распознаётся по случайному ID, созданному для твоего устройства.",
  "Ты можешь удалить аккаунт и его данные в любой момент прямо в игре."],
 h_col="Какие данные мы собираем", th=("Данные", "Цель"), rows=[
  ("Случайный ID игрока и токен входа", "Распознать игровой аккаунт и подключить тебя к серверу"),
  ("Выбранный ник, аватар и баннер, уровень, выставленные значки", "Показывать твой профиль другим игрокам (рейтинги, матчи, друзья)"),
  ("Игровая статистика и рекорды (лучшие результаты, сыгранные игры, убранные линии, победы/поражения в дуэлях, серия)", "Рейтинги, статистика профиля, подбор соперников"),
  ("Очки ранга, итоги сезонов, история матчей и счёт личных встреч", "Рейтинговый подбор, сезоны, история матчей"),
  ("Код друга, список друзей и заявки", "Друзья, статус «в сети» и приглашения"),
  ("Запись ходов в классическом режиме / режиме на время (расстановка фигур и время)", "Проверка подлинности рекордов; после проверки не хранится"),
  ("IP-адрес", "Технически нужен для подключения к серверу; не хранится в базе игроков")],
 local="Настройки (звук, музыка, язык и т. д.), локальные рекорды и прогресс также хранятся на твоём устройстве.",
 h_share="Передача данных", share="Мы не продаём и не сдаём твои данные в аренду и не передаём их рекламодателям или брокерам данных. Твой ник, аватар, баннер, уровень, значки, ранг и публичная статистика видны другим игрокам. При нажатии «Поделиться» игра создаёт изображение на устройстве и открывает меню Android «Поделиться»; изображение уходит только туда, куда выберешь ты.",
 h_sec="Хранение и безопасность", sec="Данные аккаунта хранятся на нашем игровом сервере — виртуальном выделенном сервере Natro (Турция). Трафик между игрой и сервером зашифрован (DTLS), и игра подключается только к сертификату нашего сервера. Данные сервера ежедневно резервируются; копии хранятся 14 дней и затем удаляются автоматически.",
 h_ret="Срок хранения и удаление", ret="Мы храним данные, пока существует твой аккаунт. Удалить его можно в любой момент в игре: <strong>Настройки → Удалить аккаунт</strong>. Профиль, ранг, рекорды, статистика, друзья, код друга и история матчей сразу удаляются с сервера и устройства, а ты исчезаешь из списков друзей других игроков. Копии в резервных архивах удаляются в течение 14 дней. Если игра уже не установлена, см. {del}.",
 ret2="В истории матчей других игроков может остаться прошлый матч против «Удалённый игрок» — без каких-либо твоих персональных данных.",
 del_link="Удаление аккаунта",
 h_rights="Твои права", rights="В зависимости от места проживания (например, по GDPR или турецкому закону KVKK) у тебя может быть право на доступ, исправление, удаление данных и возражение против их обработки, а также право подать жалобу в орган по защите данных. Для этого напиши нам на адрес ниже, указав ник и код друга (виден в разделе «Друзья»).",
 h_kids="Дети", kids="Игра не запрашивает персональные данные, такие как имя или контакты. Мы сознательно не собираем персональные данные детей младше 13 лет. Если ты считаешь, что ребёнок передал нам такие данные, напиши нам — мы их удалим.",
 h_chg="Изменения", chg="Если политика изменится, мы обновим эту страницу и дату выше. О существенных изменениях также сообщим в игре.",
 h_contact="Контакты", lang_label="Язык"),
"zh": dict(
 title="Crossblocks 隐私政策", date="生效日期：2026年9月28日",
 intro="本政策说明手机游戏 Crossblocks（“本游戏”“我们”）收集哪些信息、为何收集，以及你有哪些选择。Crossblocks 由 256 Games (Onur Kansoy) 开发，并由其担任数据控制者。",
 h_sum="概要", sum=["无广告、无分析统计、无追踪，也没有收集数据的第三方 SDK。",
  "不收集真实姓名、电子邮箱、电话号码、通讯录、位置或照片。",
  "在线功能使用一个游戏账号，通过为你的设备随机生成的 ID 识别。",
  "你可以随时在游戏内删除账号及其数据。"],
 h_col="我们收集的信息", th=("数据", "用途"), rows=[
  ("随机玩家 ID 和登录令牌", "识别你的游戏账号并登录游戏服务器"),
  ("你选择的昵称、头像和横幅、等级、展示的徽章", "向其他玩家展示你的资料（排行榜、对战、好友）"),
  ("游戏统计和纪录（最高分、游戏局数、消除行数、对战胜负、连续天数）", "排行榜、资料统计、匹配"),
  ("段位积分、赛季结果、对战记录和双方交手战绩", "排位匹配、赛季、对战记录"),
  ("好友码、好友列表和好友请求", "好友、在线状态和邀请"),
  ("经典 / 限时模式的操作记录（方块位置和时间）", "验证排行榜纪录的真实性；验证后不保存"),
  ("IP 地址", "连接游戏服务器的技术需要；不保存在玩家数据库中")],
 local="设置（音效、音乐、语言等）、本地纪录和进度也保存在你的设备上。",
 h_share="共享", share="我们不会出售或出租你的数据，也不会与广告商或数据经纪商共享。你的昵称、头像、横幅、等级、徽章、段位和公开统计对其他玩家可见。使用“分享”按钮时，游戏会在你的设备上生成一张图片并打开 Android 分享菜单；图片只会发送到你选择的地方。",
 h_sec="存储与安全", sec="账号数据存储在我们的游戏服务器上，这是一台由 Natro（土耳其）提供的虚拟专用服务器。游戏与服务器之间的通信经过加密（DTLS），游戏只信任我们服务器的证书。服务器数据每天备份，备份保留 14 天后自动删除。",
 h_ret="保留与删除", ret="账号存在期间我们会保留你的账号数据。你可以随时在游戏中删除账号：<strong>设置 → 删除账号</strong>。这会立即从服务器和你的设备上删除你的资料、段位、纪录、统计、好友、好友码和对战记录，并将你从其他玩家的好友列表中移除。备份中的副本会在 14 天内删除。如果你已卸载游戏，请参阅{del}。",
 ret2="其他玩家的对战记录中可能仍会显示与“已删除的玩家”的旧对局，但不会关联你的任何个人数据。",
 del_link="删除账号",
 h_rights="你的权利", rights="根据你所在地区的法律（例如 GDPR 或土耳其 KVKK），你可能有权访问、更正、删除你的数据或反对其处理，并有权向数据保护机构投诉。如需行使这些权利，请发邮件至下方地址，并注明你的昵称和好友码（在好友面板中显示）。",
 h_kids="儿童", kids="本游戏不会要求提供姓名或联系方式等个人信息。我们不会在知情的情况下收集 13 岁以下儿童的个人信息。如果你认为有儿童向我们提供了个人信息，请联系我们，我们会将其删除。",
 h_chg="变更", chg="如本政策有变更，我们会更新本页面和上方的日期。重要变更也会在游戏中公告。",
 h_contact="联系方式", lang_label="语言"),
"ja": dict(
 title="Crossblocks プライバシーポリシー", date="施行日：2026年9月28日",
 intro="本ポリシーは、モバイルゲーム Crossblocks（以下「本ゲーム」「当方」）がどのような情報をなぜ収集するのか、またあなたが選べることについて説明します。Crossblocks は 256 Games (Onur Kansoy) が開発しており、同人がデータ管理者です。",
 h_sum="概要", sum=["広告、分析、トラッキング、データを収集するサードパーティ SDK は一切ありません。",
  "本名、メールアドレス、電話番号、連絡先、位置情報、写真は収集しません。",
  "オンライン機能は、端末ごとにランダムに作成される ID で識別されるゲームアカウントを使用します。",
  "アカウントとそのデータは、いつでもゲーム内から削除できます。"],
 h_col="収集する情報", th=("データ", "目的"), rows=[
  ("ランダムなプレイヤー ID とログイントークン", "ゲームアカウントの識別とゲームサーバーへのログイン"),
  ("選択したニックネーム、アバター、バナー、レベル、展示中のバッジ", "他のプレイヤーへのプロフィール表示（ランキング、対戦、フレンド）"),
  ("ゲームの統計と記録（ベストスコア、プレイ回数、消去ライン数、対戦の勝敗、連続記録）", "ランキング、プロフィール統計、マッチング"),
  ("ランクポイント、シーズン結果、対戦履歴、対戦相手との通算成績", "ランクマッチ、シーズン、対戦履歴"),
  ("フレンドコード、フレンドリスト、フレンド申請", "フレンド、オンライン状態、招待"),
  ("クラシック／タイムアタックの操作記録（ピースの配置と時間）", "ランキング記録が正当であることの確認（確認後は保存しません）"),
  ("IP アドレス", "ゲームサーバーへの接続に技術的に必要（プレイヤーデータベースには保存しません）")],
 local="設定（サウンド、音楽、言語など）、ローカル記録、進行状況はあなたの端末にも保存されます。",
 h_share="共有", share="当方はあなたのデータを販売・貸与せず、広告主やデータブローカーと共有しません。ニックネーム、アバター、バナー、レベル、バッジ、ランク、公開統計は他のプレイヤーに表示されます。「シェア」ボタンを使うと、ゲームは端末上で画像を作成し Android の共有メニューを開きます。画像はあなたが選んだ送信先にのみ送られます。",
 h_sec="保存とセキュリティ", sec="アカウントデータは、Natro（トルコ）が提供する仮想専用サーバー上のゲームサーバーに保存されます。ゲームとサーバー間の通信は暗号化（DTLS）されており、ゲームは当方サーバーの証明書にのみ接続します。サーバーデータは毎日バックアップされ、バックアップは 14 日間保管された後に自動で削除されます。",
 h_ret="保存期間と削除", ret="アカウントが存在する間、データを保存します。アカウントはゲーム内からいつでも削除できます：<strong>設定 → アカウント削除</strong>。プロフィール、ランク、記録、統計、フレンド、フレンドコード、対戦履歴がサーバーと端末から直ちに削除され、他のプレイヤーのフレンドリストからも外れます。バックアップ内のコピーは 14 日以内に削除されます。ゲームをアンインストール済みの場合は{del}をご覧ください。",
 ret2="他のプレイヤーの対戦履歴には「削除されたプレイヤー」との過去の対戦が残る場合がありますが、あなたの個人データは紐付いていません。",
 del_link="アカウントの削除",
 h_rights="あなたの権利", rights="お住まいの地域の法律（GDPR やトルコの KVKK など）により、データへのアクセス、訂正、削除、処理への異議申し立て、およびデータ保護機関への苦情申し立ての権利がある場合があります。これらの権利を行使するには、ニックネームとフレンドコード（フレンド画面に表示）を記載のうえ、下記アドレスまでご連絡ください。",
 h_kids="子どもについて", kids="本ゲームは名前や連絡先などの個人情報を求めません。13 歳未満の子どもの個人情報を故意に収集することはありません。子どもが個人情報を提供したと思われる場合はご連絡ください。削除いたします。",
 h_chg="変更", chg="本ポリシーを変更した場合は、このページと上記の日付を更新します。重要な変更はゲーム内でもお知らせします。",
 h_contact="お問い合わせ", lang_label="言語"),
"ko": dict(
 title="Crossblocks 개인정보 처리방침", date="시행일: 2026년 9월 28일",
 intro="이 방침은 모바일 게임 Crossblocks(\"게임\", \"당사\")가 어떤 정보를 왜 수집하는지, 그리고 여러분이 선택할 수 있는 사항을 설명합니다. Crossblocks는 256 Games (Onur Kansoy)가 개발했으며, 개인정보 처리 책임자입니다.",
 h_sum="요약", sum=["광고, 분석, 추적 및 데이터를 수집하는 제3자 SDK가 없습니다.",
  "실명, 이메일, 전화번호, 연락처, 위치, 사진을 수집하지 않습니다.",
  "온라인 기능은 기기마다 무작위로 생성된 ID로 식별되는 게임 계정을 사용합니다.",
  "언제든지 게임 안에서 계정과 데이터를 삭제할 수 있습니다."],
 h_col="수집하는 정보", th=("데이터", "목적"), rows=[
  ("무작위 플레이어 ID와 로그인 토큰", "게임 계정 식별 및 게임 서버 로그인"),
  ("직접 정한 닉네임, 선택한 아바타와 배너, 레벨, 전시한 배지", "다른 플레이어에게 프로필 표시(랭킹, 대전, 친구)"),
  ("게임 통계와 기록(최고 점수, 플레이 횟수, 지운 줄 수, 대전 승/패, 연속 기록)", "랭킹, 프로필 통계, 매칭"),
  ("랭크 점수, 시즌 결과, 대전 기록 및 상대 전적", "랭크 매칭, 시즌, 대전 기록"),
  ("친구 코드, 친구 목록 및 친구 요청", "친구, 온라인 상태 및 초대"),
  ("클래식 / 타임 어택 게임의 조작 기록(블록 배치와 시간)", "랭킹 기록의 진위 확인, 확인 후 저장하지 않음"),
  ("IP 주소", "게임 서버 연결에 기술적으로 필요, 플레이어 데이터베이스에 저장하지 않음")],
 local="설정(효과음, 음악, 언어 등), 로컬 기록 및 진행 상황은 기기에도 저장됩니다.",
 h_share="공유", share="당사는 여러분의 데이터를 판매하거나 대여하지 않으며 광고주나 데이터 브로커와 공유하지 않습니다. 닉네임, 아바타, 배너, 레벨, 배지, 랭크 및 공개 통계는 다른 플레이어에게 표시됩니다. \"공유\" 버튼을 누르면 게임이 기기에서 이미지를 만들고 Android 공유 메뉴를 엽니다. 이미지는 여러분이 선택한 곳으로만 전송됩니다.",
 h_sec="저장 및 보안", sec="계정 데이터는 Natro(튀르키예)가 제공하는 가상 사설 서버인 당사 게임 서버에 저장됩니다. 게임과 서버 간 통신은 암호화(DTLS)되며, 게임은 당사 서버의 인증서에만 연결합니다. 서버 데이터는 매일 백업되며, 백업은 14일간 보관된 후 자동으로 삭제됩니다.",
 h_ret="보관 및 삭제", ret="계정이 존재하는 동안 데이터를 보관합니다. 게임에서 언제든지 계정을 삭제할 수 있습니다: <strong>설정 → 계정 삭제</strong>. 프로필, 랭크, 기록, 통계, 친구, 친구 코드 및 대전 기록이 서버와 기기에서 즉시 삭제되며, 다른 플레이어의 친구 목록에서도 제거됩니다. 백업의 사본은 14일 이내에 삭제됩니다. 게임이 설치되어 있지 않다면 {del}을(를) 참고하세요.",
 ret2="다른 플레이어의 대전 기록에는 \"삭제된 플레이어\"와의 지난 대전이 남을 수 있지만, 여러분의 개인정보는 연결되지 않습니다.",
 del_link="계정 삭제",
 h_rights="여러분의 권리", rights="거주 지역의 법률(예: GDPR, 튀르키예 KVKK, 한국 개인정보 보호법)에 따라 개인정보 열람, 정정, 삭제, 처리 정지를 요구하고 개인정보 보호 기관에 민원을 제기할 권리가 있을 수 있습니다. 권리를 행사하려면 닉네임과 친구 코드(친구 화면에 표시)를 적어 아래 주소로 연락해 주세요.",
 h_kids="아동", kids="게임은 이름이나 연락처 같은 개인정보를 요구하지 않습니다. 당사는 13세 미만 아동의 개인정보를 고의로 수집하지 않습니다. 아동이 개인정보를 제공했다고 생각되면 연락해 주세요. 삭제하겠습니다.",
 h_chg="변경", chg="이 방침이 변경되면 이 페이지와 위의 날짜를 업데이트합니다. 중요한 변경 사항은 게임에서도 공지합니다.",
 h_contact="연락처", lang_label="언어"),
}

# --- hesap silme sayfası ---
D = {
"en": dict(title="Delete your Crossblocks account", sub="Crossblocks · developer: 256 Games (Onur Kansoy)",
 h_in="In the game (instant)", steps=["Open Crossblocks and tap the <strong>Settings</strong> (gear) button on the main menu.", "Tap <strong>Delete account</strong> and confirm with <strong>Delete</strong>."],
 in_note="An internet connection is required. Your account is deleted immediately.",
 h_mail="Without the game (by email)", subject="Crossblocks account deletion",
 mail="Email {email} with the subject \"Crossblocks account deletion\" and include your <strong>nickname</strong> and, if you know it, your <strong>friend code</strong> (shown in the Friends panel). We will delete the account within 30 days and reply to confirm.",
 h_what="What is deleted", what=["Profile: nickname, avatar, banner, level, badges", "Rank points, season results, records, statistics", "Friend code, friends list and friend requests (you are also removed from other players' lists)", "Match history and head-to-head results", "The player ID and login token of the account"],
 keep="Server backups are kept for up to 14 days, after which the deleted data is gone from backups as well. Other players' match histories may still show a past match against \"Deleted player\", with no personal data attached. Nothing is retained for other purposes.",
 privacy="Privacy policy"),
"tr": dict(title="Crossblocks hesabını silme", sub="Crossblocks · geliştirici: 256 Games (Onur Kansoy)",
 h_in="Oyunun içinden (anında)", steps=["Crossblocks'u aç, ana menüde <strong>Ayarlar</strong> (dişli) düğmesine dokun.", "<strong>Hesabı sil</strong>'e dokun ve <strong>Sil</strong> ile onayla."],
 in_note="İnternet bağlantısı gerekir. Hesabın hemen silinir.",
 h_mail="Oyun olmadan (e-postayla)", subject="Crossblocks hesap silme",
 mail="{email} adresine \"Crossblocks hesap silme\" konulu bir e-posta gönder; <strong>takma adını</strong> ve biliyorsan <strong>arkadaş kodunu</strong> (Arkadaşlar panelinde görünür) yaz. Hesabın 30 gün içinde silinir ve sana onay yanıtı gönderilir.",
 h_what="Neler silinir", what=["Profil: takma ad, avatar, afiş, seviye, rozetler", "Rank puanı, sezon sonuçları, rekorlar, istatistikler", "Arkadaş kodu, arkadaş listesi ve istekler (diğer oyuncuların listelerinden de çıkarılırsın)", "Maç geçmişi ve rakiplere karşı skorlar", "Hesabın oyuncu kimliği ve giriş anahtarı"],
 keep="Sunucu yedekleri en fazla 14 gün saklanır; sonrasında silinen veri yedeklerden de kalkar. Diğer oyuncuların maç geçmişinde seninle yapılmış eski bir maç, kişisel veri olmadan \"Silinmiş oyuncu\" olarak görünebilir. Başka bir amaçla veri saklanmaz.",
 privacy="Gizlilik politikası"),
"es": dict(title="Eliminar tu cuenta de Crossblocks", sub="Crossblocks · desarrollador: 256 Games (Onur Kansoy)",
 h_in="Desde el juego (al instante)", steps=["Abre Crossblocks y toca el botón de <strong>Ajustes</strong> (engranaje) en el menú principal.", "Toca <strong>Borrar cuenta</strong> y confirma con <strong>Borrar</strong>."],
 in_note="Se necesita conexión a internet. La cuenta se elimina de inmediato.",
 h_mail="Sin el juego (por correo)", subject="Eliminar cuenta de Crossblocks",
 mail="Escribe a {email} con el asunto \"Eliminar cuenta de Crossblocks\" e indica tu <strong>apodo</strong> y, si lo sabes, tu <strong>código de amigo</strong> (visible en el panel de amigos). Eliminaremos la cuenta en un plazo de 30 días y te responderemos para confirmarlo.",
 h_what="Qué se elimina", what=["Perfil: apodo, avatar, estandarte, nivel, insignias", "Puntos de rango, resultados de temporada, récords, estadísticas", "Código de amigo, lista de amigos y solicitudes (también se te quita de las listas de otros jugadores)", "Historial de partidas y resultados directos", "El ID de jugador y el token de inicio de sesión de la cuenta"],
 keep="Las copias de seguridad del servidor se guardan hasta 14 días; después, los datos eliminados desaparecen también de ellas. El historial de otros jugadores puede mostrar una partida pasada contra \"Jugador eliminado\", sin datos personales asociados. No se conserva nada con otros fines.",
 privacy="Política de privacidad"),
"de": dict(title="Crossblocks-Konto löschen", sub="Crossblocks · Entwickler: 256 Games (Onur Kansoy)",
 h_in="Im Spiel (sofort)", steps=["Öffne Crossblocks und tippe im Hauptmenü auf <strong>Einstellungen</strong> (Zahnrad).", "Tippe auf <strong>Konto löschen</strong> und bestätige mit <strong>Löschen</strong>."],
 in_note="Eine Internetverbindung ist nötig. Dein Konto wird sofort gelöscht.",
 h_mail="Ohne das Spiel (per E-Mail)", subject="Crossblocks Konto löschen",
 mail="Schreibe an {email} mit dem Betreff \"Crossblocks Konto löschen\" und gib deinen <strong>Spitznamen</strong> und, falls bekannt, deinen <strong>Freundescode</strong> (im Freunde-Bereich sichtbar) an. Wir löschen das Konto innerhalb von 30 Tagen und bestätigen es dir per Antwort.",
 h_what="Was gelöscht wird", what=["Profil: Spitzname, Avatar, Banner, Stufe, Abzeichen", "Ranglistenpunkte, Saisonergebnisse, Rekorde, Statistiken", "Freundescode, Freundesliste und Anfragen (du wirst auch aus den Listen anderer Spieler entfernt)", "Spielverlauf und direkte Bilanz", "Spieler-ID und Anmelde-Token des Kontos"],
 keep="Server-Sicherungen werden bis zu 14 Tage aufbewahrt; danach sind die gelöschten Daten auch dort entfernt. Im Spielverlauf anderer Spieler kann ein früheres Match gegen \"Gelöschter Spieler\" erscheinen, ohne personenbezogene Daten. Zu anderen Zwecken wird nichts aufbewahrt.",
 privacy="Datenschutzerklärung"),
"fr": dict(title="Supprimer ton compte Crossblocks", sub="Crossblocks · développeur : 256 Games (Onur Kansoy)",
 h_in="Dans le jeu (immédiat)", steps=["Ouvre Crossblocks et touche le bouton <strong>Paramètres</strong> (engrenage) du menu principal.", "Touche <strong>Supprimer le compte</strong> et confirme avec <strong>Supprimer</strong>."],
 in_note="Une connexion internet est nécessaire. Ton compte est supprimé immédiatement.",
 h_mail="Sans le jeu (par e-mail)", subject="Suppression de compte Crossblocks",
 mail="Écris à {email} avec l'objet « Suppression de compte Crossblocks » en indiquant ton <strong>pseudo</strong> et, si tu le connais, ton <strong>code ami</strong> (visible dans le panneau Amis). Nous supprimerons le compte sous 30 jours et te répondrons pour confirmer.",
 h_what="Ce qui est supprimé", what=["Profil : pseudo, avatar, bannière, niveau, badges", "Points de rang, résultats de saison, records, statistiques", "Code ami, liste d'amis et demandes (tu es aussi retiré des listes des autres joueurs)", "Historique des matchs et bilans face à face", "L'identifiant de joueur et le jeton de connexion du compte"],
 keep="Les sauvegardes du serveur sont conservées jusqu'à 14 jours ; ensuite, les données supprimées disparaissent aussi des sauvegardes. L'historique d'autres joueurs peut montrer un ancien match contre « Joueur supprimé », sans donnée personnelle. Rien n'est conservé à d'autres fins.",
 privacy="Politique de confidentialité"),
"pt": dict(title="Excluir sua conta do Crossblocks", sub="Crossblocks · desenvolvedor: 256 Games (Onur Kansoy)",
 h_in="No jogo (na hora)", steps=["Abra o Crossblocks e toque no botão <strong>Configurações</strong> (engrenagem) no menu principal.", "Toque em <strong>Excluir conta</strong> e confirme com <strong>Excluir</strong>."],
 in_note="É preciso estar conectado à internet. A conta é excluída imediatamente.",
 h_mail="Sem o jogo (por e-mail)", subject="Exclusão de conta do Crossblocks",
 mail="Envie um e-mail para {email} com o assunto \"Exclusão de conta do Crossblocks\" informando seu <strong>apelido</strong> e, se souber, seu <strong>código de amigo</strong> (visível no painel de amigos). Excluiremos a conta em até 30 dias e responderemos para confirmar.",
 h_what="O que é excluído", what=["Perfil: apelido, avatar, banner, nível, emblemas", "Pontos de rank, resultados de temporada, recordes, estatísticas", "Código de amigo, lista de amigos e pedidos (você também sai das listas de outros jogadores)", "Histórico de partidas e confrontos diretos", "O ID de jogador e o token de login da conta"],
 keep="Os backups do servidor são mantidos por até 14 dias; depois disso, os dados excluídos também somem dos backups. O histórico de outros jogadores pode mostrar uma partida antiga contra \"Jogador excluído\", sem dados pessoais. Nada é mantido para outros fins.",
 privacy="Política de privacidade"),
"it": dict(title="Eliminare l'account Crossblocks", sub="Crossblocks · sviluppatore: 256 Games (Onur Kansoy)",
 h_in="Dal gioco (subito)", steps=["Apri Crossblocks e tocca il pulsante <strong>Impostazioni</strong> (ingranaggio) nel menu principale.", "Tocca <strong>Elimina account</strong> e conferma con <strong>Elimina</strong>."],
 in_note="Serve una connessione a internet. L'account viene eliminato subito.",
 h_mail="Senza il gioco (via e-mail)", subject="Eliminazione account Crossblocks",
 mail="Scrivi a {email} con oggetto \"Eliminazione account Crossblocks\" indicando il tuo <strong>nickname</strong> e, se lo conosci, il tuo <strong>codice amico</strong> (visibile nel pannello Amici). Elimineremo l'account entro 30 giorni e ti risponderemo per conferma.",
 h_what="Cosa viene eliminato", what=["Profilo: nickname, avatar, stendardo, livello, distintivi", "Punti rango, risultati stagionali, record, statistiche", "Codice amico, lista amici e richieste (vieni rimosso anche dalle liste degli altri giocatori)", "Cronologia partite e scontri diretti", "L'ID giocatore e il token di accesso dell'account"],
 keep="I backup del server sono conservati fino a 14 giorni; dopo, i dati eliminati spariscono anche dai backup. La cronologia di altri giocatori può mostrare una vecchia partita contro \"Giocatore eliminato\", senza dati personali. Nulla viene conservato per altri scopi.",
 privacy="Informativa sulla privacy"),
"ru": dict(title="Удаление аккаунта Crossblocks", sub="Crossblocks · разработчик: 256 Games (Onur Kansoy)",
 h_in="В игре (сразу)", steps=["Открой Crossblocks и нажми кнопку <strong>Настройки</strong> (шестерёнка) в главном меню.", "Нажми <strong>Удалить аккаунт</strong> и подтверди кнопкой <strong>Удалить</strong>."],
 in_note="Нужно подключение к интернету. Аккаунт удаляется сразу.",
 h_mail="Без игры (по e-mail)", subject="Удаление аккаунта Crossblocks",
 mail="Напиши на {email} с темой «Удаление аккаунта Crossblocks» и укажи свой <strong>ник</strong> и, если знаешь, <strong>код друга</strong> (виден в разделе «Друзья»). Мы удалим аккаунт в течение 30 дней и ответим с подтверждением.",
 h_what="Что удаляется", what=["Профиль: ник, аватар, баннер, уровень, значки", "Очки ранга, итоги сезонов, рекорды, статистика", "Код друга, список друзей и заявки (ты также исчезаешь из списков других игроков)", "История матчей и счёт личных встреч", "ID игрока и токен входа аккаунта"],
 keep="Резервные копии сервера хранятся до 14 дней, после чего удалённые данные исчезают и из них. В истории других игроков может остаться прошлый матч против «Удалённый игрок» — без персональных данных. Ничего не хранится для других целей.",
 privacy="Политика конфиденциальности"),
"zh": dict(title="删除你的 Crossblocks 账号", sub="Crossblocks · 开发者：256 Games (Onur Kansoy)",
 h_in="在游戏中（立即生效）", steps=["打开 Crossblocks，点击主菜单上的<strong>设置</strong>（齿轮）按钮。", "点击<strong>删除账号</strong>，并点击<strong>删除</strong>确认。"],
 in_note="需要联网。账号会立即删除。",
 h_mail="不通过游戏（发送邮件）", subject="删除 Crossblocks 账号",
 mail="发送邮件至 {email}，主题为“删除 Crossblocks 账号”，并写明你的<strong>昵称</strong>以及（如知道）<strong>好友码</strong>（在好友面板中显示）。我们会在 30 天内删除账号并回复确认。",
 h_what="删除的内容", what=["资料：昵称、头像、横幅、等级、徽章", "段位积分、赛季结果、纪录、统计", "好友码、好友列表和请求（你也会从其他玩家的列表中移除）", "对战记录和交手战绩", "账号的玩家 ID 和登录令牌"],
 keep="服务器备份最多保留 14 天，之后已删除的数据也会从备份中消失。其他玩家的对战记录中可能仍显示与“已删除的玩家”的旧对局，但不含个人数据。不会出于其他目的保留任何数据。",
 privacy="隐私政策"),
"ja": dict(title="Crossblocks アカウントの削除", sub="Crossblocks · 開発者：256 Games (Onur Kansoy)",
 h_in="ゲーム内で（すぐに削除）", steps=["Crossblocks を開き、メインメニューの<strong>設定</strong>（歯車）ボタンをタップします。", "<strong>アカウント削除</strong>をタップし、<strong>削除</strong>で確定します。"],
 in_note="インターネット接続が必要です。アカウントはすぐに削除されます。",
 h_mail="ゲームを使わずに（メールで）", subject="Crossblocks アカウント削除",
 mail="{email} 宛に件名「Crossblocks アカウント削除」でメールを送り、<strong>ニックネーム</strong>と、わかれば<strong>フレンドコード</strong>（フレンド画面に表示）を記載してください。30 日以内にアカウントを削除し、確認のご返信をします。",
 h_what="削除される内容", what=["プロフィール：ニックネーム、アバター、バナー、レベル、バッジ", "ランクポイント、シーズン結果、記録、統計", "フレンドコード、フレンドリスト、申請（他のプレイヤーのリストからも外れます）", "対戦履歴と通算成績", "アカウントのプレイヤー ID とログイントークン"],
 keep="サーバーのバックアップは最長 14 日間保管され、その後は削除済みのデータもバックアップから消えます。他のプレイヤーの対戦履歴に「削除されたプレイヤー」との過去の対戦が表示される場合がありますが、個人データは含まれません。その他の目的でデータを保持することはありません。",
 privacy="プライバシーポリシー"),
"ko": dict(title="Crossblocks 계정 삭제", sub="Crossblocks · 개발자: 256 Games (Onur Kansoy)",
 h_in="게임에서 (즉시)", steps=["Crossblocks를 열고 메인 메뉴의 <strong>설정</strong>(톱니바퀴) 버튼을 누릅니다.", "<strong>계정 삭제</strong>를 누르고 <strong>삭제</strong>로 확인합니다."],
 in_note="인터넷 연결이 필요합니다. 계정은 즉시 삭제됩니다.",
 h_mail="게임 없이 (이메일)", subject="Crossblocks 계정 삭제",
 mail="{email}(으)로 제목을 \"Crossblocks 계정 삭제\"로 하여 이메일을 보내고 <strong>닉네임</strong>과, 알고 있다면 <strong>친구 코드</strong>(친구 화면에 표시)를 적어 주세요. 30일 이내에 계정을 삭제하고 확인 답장을 드립니다.",
 h_what="삭제되는 항목", what=["프로필: 닉네임, 아바타, 배너, 레벨, 배지", "랭크 점수, 시즌 결과, 기록, 통계", "친구 코드, 친구 목록 및 요청(다른 플레이어의 목록에서도 제거됨)", "대전 기록 및 상대 전적", "계정의 플레이어 ID와 로그인 토큰"],
 keep="서버 백업은 최대 14일간 보관되며, 그 후에는 삭제된 데이터가 백업에서도 사라집니다. 다른 플레이어의 대전 기록에는 개인정보 없이 \"삭제된 플레이어\"와의 지난 대전이 표시될 수 있습니다. 다른 목적으로 보관하는 데이터는 없습니다.",
 privacy="개인정보 처리방침"),
}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="google" content="notranslate">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<nav><label>🌐 <select id="lang" aria-label="Language">{options}</select></label>{extra}</nav>
"""

SCRIPT = """</main>
<script>
// dil: ?lang= (oyun Lang.code gönderir, ör. pt_BR, zh_CN) ya da tarayıcı dili; yoksa İngilizce
(function(){
  var langs = %s;
  function pick(v){ v = (v || "").toLowerCase().replace("_", "-").split("-")[0]; return langs.indexOf(v) >= 0 ? v : "en"; }
  function show(l){
    document.documentElement.lang = l;
    langs.forEach(function(x){ document.getElementById(x).hidden = x !== l; });
    document.getElementById("lang").value = l;
    document.querySelectorAll("a[data-keep-lang]").forEach(function(a){ a.href = a.getAttribute("data-keep-lang") + "?lang=" + l; });
    var t = document.getElementById(l).getAttribute("data-title"); if (t) document.title = t;
  }
  var q = new URLSearchParams(location.search).get("lang");
  show(pick(q || navigator.language));
  document.getElementById("lang").addEventListener("change", function(e){
    show(e.target.value); history.replaceState(null, "", "?lang=" + e.target.value);
  });
})();
</script>
</body>
</html>
""" % str(LANGS).replace("'", '"')

def options():
    return "".join('<option value="%s">%s</option>' % (l, NAMES[l]) for l in LANGS)

def mailto(subject):
    import urllib.parse
    return '<a href="mailto:%s?subject=%s">%s</a>' % (EMAIL, urllib.parse.quote(subject), EMAIL)

def privacy():
    out = [HEAD.format(title=P["en"]["title"], options=options(),
        extra='<a data-keep-lang="delete.html" href="delete.html">🗑</a>')]
    for l in LANGS:
        p = P[l]
        rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (html.escape(a), html.escape(b)) for a, b in p["rows"])
        dl = '<a data-keep-lang="delete.html" href="delete.html">%s</a>' % html.escape(p["del_link"])
        out.append(f'''<section id="{l}" lang="{l}" data-title="{html.escape(p['title'])}"{' hidden' if l != 'en' else ''}>
<h1>{html.escape(p['title'])}</h1>
<p class="muted">{html.escape(p['date'])}</p>
<p>{html.escape(p['intro'])}</p>
<h2>{p['h_sum']}</h2>
<ul>{''.join('<li>%s</li>' % html.escape(x) for x in p['sum'])}</ul>
<h2>{p['h_col']}</h2>
<div class="wrap"><table><tr><th>{p['th'][0]}</th><th>{p['th'][1]}</th></tr>{rows}</table></div>
<p>{html.escape(p['local'])}</p>
<h2>{p['h_share']}</h2>
<p>{html.escape(p['share'])}</p>
<h2>{p['h_sec']}</h2>
<p>{html.escape(p['sec'])}</p>
<h2>{p['h_ret']}</h2>
<p>{p['ret'].replace('{del}', dl)}</p>
<p>{html.escape(p['ret2'])}</p>
<h2>{p['h_rights']}</h2>
<p>{html.escape(p['rights'])}</p>
<h2>{p['h_kids']}</h2>
<p>{html.escape(p['kids'])}</p>
<h2>{p['h_chg']}</h2>
<p>{html.escape(p['chg'])}</p>
<h2>{p['h_contact']}</h2>
<p>256 Games (Onur Kansoy) — <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</section>
''')
    out.append(SCRIPT)
    return "".join(out)

def deletion():
    out = [HEAD.format(title=D["en"]["title"], options=options(), extra="")]
    for l in LANGS:
        d = D[l]
        steps = "".join("<li>%s</li>" % s for s in d["steps"])
        what = "".join("<li>%s</li>" % html.escape(w) for w in d["what"])
        out.append(f'''<section id="{l}" lang="{l}" data-title="{html.escape(d['title'])}"{' hidden' if l != 'en' else ''}>
<h1>{html.escape(d['title'])}</h1>
<p class="muted">{html.escape(d['sub'])} · <a data-keep-lang="index.html" href="index.html">{html.escape(d['privacy'])}</a></p>
<div class="card">
<h2>{d['h_in']}</h2>
<ol>{steps}</ol>
<p>{html.escape(d['in_note'])}</p>
</div>
<div class="card">
<h2>{d['h_mail']}</h2>
<p>{d['mail'].replace('{email}', mailto(d['subject']))}</p>
</div>
<h2>{d['h_what']}</h2>
<ul>{what}</ul>
<p>{html.escape(d['keep'])}</p>
</section>
''')
    out.append(SCRIPT)
    return "".join(out)

if __name__ == "__main__":
    assert set(P) == set(LANGS) and set(D) == set(LANGS)
    for l in LANGS:
        assert set(P[l]) == set(P["en"]), l
        assert set(D[l]) == set(D["en"]), l
        assert len(P[l]["rows"]) == len(P["en"]["rows"]) and len(D[l]["what"]) == len(D["en"]["what"]), l
    open("index.html", "w").write(privacy())
    open("delete.html", "w").write(deletion())
    print("ok:", len(LANGS), "languages")
