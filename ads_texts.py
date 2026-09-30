"""Reklam (Google AdMob) güncellemesi için metinler: build.py bunları P sözlüğüne uygular.
Her dil: date, sum0 (özetin ilk maddesi), row (veri tablosuna ek satır), share_add (paylaşım
paragrafına ek cümle), h_ads + ads (yeni Reklamlar bölümü).
"""

ADS_URL = '<a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a>'

A = {
"en": dict(
 date="Effective date: 30 September 2026",
 sum0="The game shows ads provided by Google AdMob. We use no analytics or tracking of our own, and no other third-party SDKs that collect data.",
 row=("Advertising ID, IP address and device information (collected by Google AdMob)", "Showing and measuring ads and preventing fraud; personalized ads only with your consent where required"),
 share_add=" Ads are provided by Google AdMob, which receives the data described in the Advertising section.",
 h_ads="Advertising",
 ads="The game shows ads provided by Google AdMob: optional rewarded ads (for example, to continue a game, double the cubes you earned or repair a daily streak) and occasional ads between games. Google may collect and use your device's advertising ID, IP address and device information to show and measure ads and to prevent fraud, as described in Google's policy: {url}. In the EEA, the UK and Switzerland, the game asks for your consent with Google's consent form before personalized ads are shown; you can change your choice at any time in <strong>Settings → Privacy options</strong>. You can reset or delete your advertising ID in your device settings. Rewarded ads are always optional."),
"tr": dict(
 date="Yürürlük tarihi: 30 Eylül 2026",
 sum0="Oyun, Google AdMob tarafından sağlanan reklamlar gösterir. Kendi analiz ya da takip araçlarımız ve veri toplayan başka üçüncü taraf yazılım yoktur.",
 row=("Reklam kimliği, IP adresi ve cihaz bilgisi (Google AdMob tarafından toplanır)", "Reklam göstermek ve ölçmek, sahtekârlığı önlemek; kişiselleştirilmiş reklam yalnızca gerektiği yerde onayınla"),
 share_add=" Reklamlar, Reklamlar bölümünde anlatılan verileri alan Google AdMob tarafından sağlanır.",
 h_ads="Reklamlar",
 ads="Oyun, Google AdMob tarafından sağlanan reklamlar gösterir: isteğe bağlı ödüllü reklamlar (örneğin oyuna devam etmek, kazandığın küpleri ikiye katlamak ya da günlük seriyi onarmak için) ve oyunlar arasında zaman zaman gösterilen reklamlar. Google, reklam göstermek ve ölçmek ve sahtekârlığı önlemek için cihazının reklam kimliğini, IP adresini ve cihaz bilgilerini toplayıp kullanabilir; ayrıntılar Google'ın politikasında: {url}. AEA, Birleşik Krallık ve İsviçre'de oyun, kişiselleştirilmiş reklam göstermeden önce Google'ın onay formuyla onayını ister; seçimini istediğin zaman <strong>Ayarlar → Gizlilik seçenekleri</strong> bölümünden değiştirebilirsin. Reklam kimliğini cihazının ayarlarından sıfırlayabilir ya da silebilirsin. Ödüllü reklamlar her zaman isteğe bağlıdır."),
"es": dict(
 date="Fecha de entrada en vigor: 30 de septiembre de 2026",
 sum0="El juego muestra anuncios de Google AdMob. No usamos analíticas ni seguimiento propios, ni otros SDK de terceros que recojan datos.",
 row=("ID de publicidad, dirección IP e información del dispositivo (recogidos por Google AdMob)", "Mostrar y medir anuncios y prevenir el fraude; anuncios personalizados solo con tu consentimiento cuando sea obligatorio"),
 share_add=" Los anuncios los proporciona Google AdMob, que recibe los datos descritos en la sección Publicidad.",
 h_ads="Publicidad",
 ads="El juego muestra anuncios de Google AdMob: anuncios con recompensa opcionales (por ejemplo, para continuar una partida, duplicar los cubos ganados o reparar una racha diaria) y anuncios ocasionales entre partidas. Google puede recoger y usar el ID de publicidad de tu dispositivo, tu dirección IP e información del dispositivo para mostrar y medir anuncios y prevenir el fraude, como se describe en su política: {url}. En el EEE, el Reino Unido y Suiza, el juego te pide consentimiento con el formulario de Google antes de mostrar anuncios personalizados; puedes cambiar tu elección en cualquier momento en <strong>Ajustes → Opciones de privacidad</strong>. Puedes restablecer o eliminar tu ID de publicidad en los ajustes del dispositivo. Los anuncios con recompensa son siempre opcionales."),
"de": dict(
 date="Gültig ab: 30. September 2026",
 sum0="Das Spiel zeigt Werbung von Google AdMob. Wir nutzen keine eigene Analyse oder Nachverfolgung und keine anderen Drittanbieter-SDKs, die Daten erheben.",
 row=("Werbe-ID, IP-Adresse und Geräteinformationen (von Google AdMob erhoben)", "Werbung anzeigen und messen, Betrug verhindern; personalisierte Werbung nur mit deiner Einwilligung, wo erforderlich"),
 share_add=" Werbung wird von Google AdMob bereitgestellt, das die im Abschnitt Werbung beschriebenen Daten erhält.",
 h_ads="Werbung",
 ads="Das Spiel zeigt Werbung von Google AdMob: freiwillige Werbung mit Belohnung (zum Beispiel, um eine Runde fortzusetzen, verdiente Würfel zu verdoppeln oder eine Tagesserie zu retten) und gelegentliche Werbung zwischen Runden. Google kann die Werbe-ID deines Geräts, deine IP-Adresse und Geräteinformationen erheben und nutzen, um Werbung anzuzeigen und zu messen und Betrug zu verhindern, wie in Googles Richtlinie beschrieben: {url}. Im EWR, im Vereinigten Königreich und in der Schweiz fragt das Spiel mit dem Einwilligungsformular von Google nach deiner Einwilligung, bevor personalisierte Werbung angezeigt wird; du kannst deine Wahl jederzeit unter <strong>Einstellungen → Datenschutzoptionen</strong> ändern. Deine Werbe-ID kannst du in den Geräteeinstellungen zurücksetzen oder löschen. Werbung mit Belohnung ist immer freiwillig."),
"fr": dict(
 date="Date d'entrée en vigueur : 30 septembre 2026",
 sum0="Le jeu affiche des publicités fournies par Google AdMob. Nous n'utilisons aucun outil d'analyse ou de suivi propre, ni d'autre SDK tiers qui collecte des données.",
 row=("Identifiant publicitaire, adresse IP et informations sur l'appareil (collectés par Google AdMob)", "Afficher et mesurer les publicités, prévenir la fraude ; publicités personnalisées uniquement avec ton consentement lorsque c'est requis"),
 share_add=" Les publicités sont fournies par Google AdMob, qui reçoit les données décrites dans la section Publicité.",
 h_ads="Publicité",
 ads="Le jeu affiche des publicités fournies par Google AdMob : des publicités avec récompense facultatives (par exemple pour continuer une partie, doubler les cubes gagnés ou réparer une série quotidienne) et, de temps en temps, des publicités entre les parties. Google peut collecter et utiliser l'identifiant publicitaire de ton appareil, ton adresse IP et des informations sur l'appareil pour afficher et mesurer les publicités et prévenir la fraude, comme décrit dans sa politique : {url}. Dans l'EEE, au Royaume-Uni et en Suisse, le jeu te demande ton consentement via le formulaire de Google avant d'afficher des publicités personnalisées ; tu peux modifier ton choix à tout moment dans <strong>Paramètres → Options de confidentialité</strong>. Tu peux réinitialiser ou supprimer ton identifiant publicitaire dans les paramètres de ton appareil. Les publicités avec récompense sont toujours facultatives."),
"pt": dict(
 date="Data de vigência: 30 de setembro de 2026",
 sum0="O jogo exibe anúncios fornecidos pelo Google AdMob. Não usamos análise ou rastreamento próprios nem outros SDKs de terceiros que coletem dados.",
 row=("ID de publicidade, endereço IP e informações do dispositivo (coletados pelo Google AdMob)", "Exibir e medir anúncios e evitar fraudes; anúncios personalizados só com seu consentimento, quando exigido"),
 share_add=" Os anúncios são fornecidos pelo Google AdMob, que recebe os dados descritos na seção Publicidade.",
 h_ads="Publicidade",
 ads="O jogo exibe anúncios fornecidos pelo Google AdMob: anúncios premiados opcionais (por exemplo, para continuar uma partida, dobrar os cubos ganhos ou recuperar uma sequência diária) e anúncios ocasionais entre partidas. O Google pode coletar e usar o ID de publicidade do seu dispositivo, seu endereço IP e informações do dispositivo para exibir e medir anúncios e evitar fraudes, conforme descrito na política do Google: {url}. No EEE, no Reino Unido e na Suíça, o jogo pede seu consentimento com o formulário do Google antes de exibir anúncios personalizados; você pode mudar sua escolha a qualquer momento em <strong>Configurações → Opções de privacidade</strong>. Você pode redefinir ou excluir seu ID de publicidade nas configurações do dispositivo. Os anúncios premiados são sempre opcionais."),
"it": dict(
 date="Data di entrata in vigore: 30 settembre 2026",
 sum0="Il gioco mostra annunci forniti da Google AdMob. Non usiamo strumenti di analisi o tracciamento nostri né altri SDK di terze parti che raccolgono dati.",
 row=("ID pubblicitario, indirizzo IP e informazioni sul dispositivo (raccolti da Google AdMob)", "Mostrare e misurare gli annunci e prevenire le frodi; annunci personalizzati solo con il tuo consenso, dove richiesto"),
 share_add=" Gli annunci sono forniti da Google AdMob, che riceve i dati descritti nella sezione Pubblicità.",
 h_ads="Pubblicità",
 ads="Il gioco mostra annunci forniti da Google AdMob: annunci con premio facoltativi (ad esempio per continuare una partita, raddoppiare i cubi guadagnati o recuperare una serie giornaliera) e, di tanto in tanto, annunci tra una partita e l'altra. Google può raccogliere e usare l'ID pubblicitario del tuo dispositivo, il tuo indirizzo IP e informazioni sul dispositivo per mostrare e misurare gli annunci e prevenire le frodi, come descritto nella sua policy: {url}. Nel SEE, nel Regno Unito e in Svizzera il gioco chiede il tuo consenso con il modulo di Google prima di mostrare annunci personalizzati; puoi cambiare la tua scelta in qualsiasi momento in <strong>Impostazioni → Opzioni privacy</strong>. Puoi reimpostare o eliminare l'ID pubblicitario nelle impostazioni del dispositivo. Gli annunci con premio sono sempre facoltativi."),
"ru": dict(
 date="Дата вступления в силу: 30 сентября 2026 г.",
 sum0="В игре показывается реклама Google AdMob. Собственной аналитики и отслеживания у нас нет, других сторонних SDK, собирающих данные, тоже нет.",
 row=("Рекламный идентификатор, IP-адрес и сведения об устройстве (собирает Google AdMob)", "Показ и измерение рекламы, защита от мошенничества; персонализированная реклама — только с твоего согласия, где это требуется"),
 share_add=" Рекламу предоставляет Google AdMob, который получает данные, описанные в разделе «Реклама».",
 h_ads="Реклама",
 ads="В игре показывается реклама Google AdMob: необязательная реклама с наградой (например, чтобы продолжить игру, удвоить полученные кубы или восстановить ежедневную серию) и иногда реклама между играми. Google может собирать и использовать рекламный идентификатор устройства, IP-адрес и сведения об устройстве, чтобы показывать и измерять рекламу и предотвращать мошенничество, как описано в его политике: {url}. В ЕЭЗ, Великобритании и Швейцарии игра запрашивает твоё согласие через форму Google, прежде чем показывать персонализированную рекламу; изменить выбор можно в любое время в разделе <strong>Настройки → Параметры конфиденциальности</strong>. Рекламный идентификатор можно сбросить или удалить в настройках устройства. Реклама с наградой всегда необязательна."),
"zh": dict(
 date="生效日期：2026年9月30日",
 sum0="游戏会展示由 Google AdMob 提供的广告。我们没有自己的分析或跟踪工具，也没有其他收集数据的第三方 SDK。",
 row=("广告 ID、IP 地址和设备信息（由 Google AdMob 收集）", "展示和衡量广告、防止欺诈；仅在需要时经你同意后展示个性化广告"),
 share_add="广告由 Google AdMob 提供，它会接收“广告”部分所述的数据。",
 h_ads="广告",
 ads="游戏会展示由 Google AdMob 提供的广告：可选的激励广告（例如继续游戏、将获得的方块翻倍或修复每日连续记录）以及偶尔在两局之间出现的广告。Google 可能会收集并使用你设备的广告 ID、IP 地址和设备信息，用于展示和衡量广告及防止欺诈，详见 Google 的政策：{url}。在欧洲经济区、英国和瑞士，游戏会在展示个性化广告前通过 Google 的同意表单征求你的同意；你可以随时在<strong>设置 → 隐私选项</strong>中更改选择。你可以在设备设置中重置或删除广告 ID。激励广告始终是可选的。"),
"ja": dict(
 date="施行日：2026年9月30日",
 sum0="このゲームは Google AdMob が提供する広告を表示します。独自の分析・トラッキングは行わず、データを収集するその他のサードパーティ SDK も使用しません。",
 row=("広告 ID、IP アドレス、端末情報（Google AdMob が収集）", "広告の表示と効果測定、不正防止。パーソナライズド広告は必要な地域では同意がある場合のみ"),
 share_add="広告は Google AdMob が提供し、「広告」の項に記載のデータを受け取ります。",
 h_ads="広告",
 ads="このゲームは Google AdMob が提供する広告を表示します：任意のリワード広告（例：ゲームの続行、獲得したキューブの倍増、デイリー連続記録の修復）と、ゲームの合間にときどき表示される広告です。Google は、広告の表示・効果測定と不正防止のために、端末の広告 ID、IP アドレス、端末情報を収集・利用することがあります。詳しくは Google のポリシーをご覧ください：{url}。EEA、英国、スイスでは、パーソナライズド広告を表示する前に Google の同意フォームで同意を求めます。選択は<strong>設定 → プライバシーオプション</strong>からいつでも変更できます。広告 ID は端末の設定からリセットまたは削除できます。リワード広告は常に任意です。"),
"ko": dict(
 date="시행일: 2026년 9월 30일",
 sum0="게임은 Google AdMob이 제공하는 광고를 표시합니다. 자체 분석이나 추적 도구를 사용하지 않으며, 데이터를 수집하는 다른 서드파티 SDK도 없습니다.",
 row=("광고 ID, IP 주소 및 기기 정보(Google AdMob이 수집)", "광고 표시 및 측정, 부정 행위 방지. 맞춤형 광고는 필요한 지역에서 동의한 경우에만"),
 share_add=" 광고는 Google AdMob이 제공하며, AdMob은 '광고' 항목에 설명된 데이터를 받습니다.",
 h_ads="광고",
 ads="게임은 Google AdMob이 제공하는 광고를 표시합니다: 선택형 보상 광고(예: 게임 이어하기, 획득한 큐브 두 배, 일일 연속 기록 복구)와 게임 사이에 가끔 나오는 광고입니다. Google은 광고 표시와 측정, 부정 행위 방지를 위해 기기의 광고 ID, IP 주소 및 기기 정보를 수집하고 사용할 수 있으며, 자세한 내용은 Google 정책에 설명되어 있습니다: {url}. EEA, 영국 및 스위스에서는 맞춤형 광고를 표시하기 전에 Google 동의 양식으로 동의를 요청하며, <strong>설정 → 개인정보 보호 옵션</strong>에서 언제든지 선택을 변경할 수 있습니다. 광고 ID는 기기 설정에서 재설정하거나 삭제할 수 있습니다. 보상 광고는 언제나 선택 사항입니다."),
}


def apply(P: dict) -> None:
	for lang, a in A.items():
		p = P[lang]
		p["date"] = a["date"]
		p["sum"] = [a["sum0"]] + p["sum"][1:]
		# IP satırından önce (sonuncu), reklam verisi
		p["rows"] = p["rows"][:-1] + [a["row"]] + p["rows"][-1:]
		if a["share_add"] not in p["share"]:
			p["share"] = p["share"] + a["share_add"]
		p["h_ads"] = a["h_ads"]
		p["ads"] = a["ads"].replace("{url}", ADS_URL)
