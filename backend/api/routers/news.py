from fastapi import APIRouter
from typing import List
import schemas.news as news_schema

router = APIRouter()


@router.get("/news", response_model=List[news_schema.News])
async def list_news():
    return [
        news_schema.News(
            id=1,
            title="Cyolo 製品概要：すべての環境への安全なリモートアクセス",
            keywords={
                "OTセキュリティ": "オペレーションテクノロジーを守るために必要なセキュリティ対策",
                "ゼロトラスト": "アクセス許可において、信頼を前提にせずに認証を行うセキュリティアプローチ",
                "IdP": "ユーザーのアイデンティティを扱うサービス",
            },
            content="オペレーションテクノロジー（OT）のサイバーセキュリティは、組織の重要なシステムとリソースを保護するために必要不可欠ですが、複雑で困難な側面でもあります。最近は、サイバー犯罪者はシステムに突破するのではなくログインすることが多くなり、アクセスセキュリティがより複雑であるため管理と制御がますます重要になっています。このようなアクセス関連の課題に対処するために、Cyoloのチームは、OTおよび産業制御システム（ICS）環境の独自のセキュリティ、安全性、可用性要件を満たすゼロトラストアクセスプラットフォームを構築しています。\n\nCyoloのソリューションは、ゼロトラストネットワークアクセス（ZTNA）、Identity Provider（IdP）、Privileged Access Management（PAM）の組み合わせです。他のZTNAソリューションにはIdPまたはPAM機能がない一方、Identity and Access Managementツール（IdPとPAM）は接続性を拡張していません。Cyoloはクラウド接続またはエンドポイントエージェントのインストールを必要としないため、多くの組織が苦戦している接続性のユースケースに対処できます。 また、Cyoloは、Identity Access Controller（IDAC）とEdgeの組み合わせによって構築されており、IDACはTransport Layer Security（TLS）1.3接続を終了し、Cyolo管理者によって構成されたアクセスポリシーを強制します。IDACは逆プロキシとして機能し、すべての復号化と強制は組織のファイアウォールの後ろで行われます。EdgeはIDACに関連するSNIヘッダーに基づいてユーザーのリクエストをルーティングします。Edgeは、外部接続なしで動作することができ、トラフィックを傍受しないため、ゼロトラスト原則に準拠したまれなゼロトラストアクセスソリューションです。\n\nCyoloはオンプレミス、SaaSモデル、ハイブリッドの3つのデプロイメント方式に対応しています。必要に応じて完全に分離され、Non-IP接続されることができます。主要なコンポーネントとして、Identity providers（IdP）とIdentity Access Controller（IDAC）があります。Cyoloは既存のIdPと統合することができますし、CyoloのローカルIdPを使用することもできます。IDACはIdPに直接接続するため、Edge経由でアクセスする必要はありません。また、IDACには、ユーザーのセッションを接続するか、どの公開されたアプリケーションについてもアウトバウンド通信があるため、常にコミュニケーションが発生します。Cyoloは、一般的なIdPs（Okta、Active Directory、Azure AD、Pingなど）とも連携することができます。マルチファクタ認証（MFA）などの追加認証ステップを要求することもできます。\n\nCyoloは、有効なアイデンティティに基づいてすべてのアプリケーションに接続し、ユーザーのためにクレデンシャルを挿入して完全なシングルサインオン（SSO）エクスペリエンスを実現します。また、Cyoloはセキュリティアサーションマークアップ言語（SAML）やOpenID Connect（OIDC）で通信しない旧式の機器やシステム向けに、MFAおよびSSOを拡張することができます。各アプリケーションは、個々のユーザーやグループ、時間帯、場所などを考慮した特定のアクセスパラメータに設定されているため、必要な権限を持つユーザーにのみアクセスが許可されます。アクセスする前に承認を要求したり、各アクセスセッションを記録したりすることもできます。プラットフォーム上のすべてのアクティビティは、容易にエクスポート可能なログとして追跡されます。Cyoloは、ゲストアクセスの追加など、OT環境の調整が困難な状況に特に役立ちます。Cyoloを利用すると、クラウド接続を必要としないため、ネットワークの重要なセグメントを分離し、アクセスを制限する必要がある企業に最適です。また、Cyoloはエージェントのインストールが必要ないため、サードパーティ、外部の請負業者、またはビジネスパートナーに使用することが容易です。",
        ),
        news_schema.News(
            id=2,
            title="CopperStealerマルウェアクルーが新しいルートキットとフィッシングキットモジュールで復活",
            keywords={
                "CopperStealer": "情報を盗むマルウェア",
                "Water Orthrus": "CopperStealerを配布するグループ",
                "CopperPhish": "クレジットカード情報を収集するフィッシングキット",
            },
            content="2023年3月と4月に、CopperStealerの背後の脅威アクターは「CopperStealth」と「CopperPhish」と呼ばれる2つの新しいペイロードを配布するためのキャンペーンを再開しました。CopperStealerを配布するこのグループはWater OrthrusとしてTrendMicroによって追跡されており、2019年にBitdefenderによって詳細が公開された別のキャンペーン、Scranosもこのグループに帰属します。このグループは、少なくとも2021年から、被害者を不正なソフトウェアのダウンロードサイトにリダイレクトするためのPPI（ペイパーインストール）ネットワークを活用し、情報盗みマルウェアCopperStealerを配布しています。新しい攻撃手法では、CopperStealthのインストーラを中国のソフトウェア共有ウェブサイトで無料配布し、CopperStealthの拡散を図っています。CopperPhishキャンペーンでは、無料の匿名ファイル共有ウェブサイトの背後にあるPPIネットワークを利用し、マルウェアを配布しています。訪問者が広告をクリックすると、ダウンロードリンクに偽装したダウンロードページにリダイレクトされ、ダウンロードされたファイルはプライベートローダーとなります。このローダーはPPI基盤で提供され、クレジットカード情報を収集するフィッシングキット、CopperPhishをダウンロードし起動します。個人情報が入力されると、CopperPhishは「ID検証に合格しました」というメッセージと、画面に入力する確認コードを表示します。正しい確認コードが提供されると、マルウェアはアンインストールされ、すべての不正なプロセスが停止し、影響を受けたデバイス上からファイルが削除されます。",
        ),
        news_schema.News(
            id=3,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=4,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=5,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=6,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=7,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=8,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=9,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
        news_schema.News(
            id=10,
            title="ハッカーはApple macOSシステムを狙うためにCobalt StrikeのGolangバリアントを使用",
            keywords={
                "Geacon": "Go言語で実装され、Apple macOSシステムを対象とするCobalt Strike",
                "Cobalt Strike": "Fortraが開発したレッドチームと対敵シミュレーションツールで、クラック版が脅威行為者により悪用されている",
                "macOS": "macOS向けの攻撃は少なく、Cobalt Strikeに関連する後方検出活動は主にWindowsに対して行われていたが、Geaconの登場により変わる可能性がある",
            },
            content="セキュリティ企業のSentinelOneはGeaconであるCobalt StrikeのGoバージョンがVirusTotalに増えており、脅威行為者がApple macOSシステムを標的としていることがわかりました。これまでCobalt Strikeの攻撃はWindows向けであったため、macOS向けの攻撃は稀であったが、Geaconの登場によって状況が変わる可能性があります。GeaconはCobalt StrikeのGoバージョンであり、GitHub上で2020年2月から利用可能である。SentinelOneによると、Geaconの2つの新しいVirusTotalサンプルの分析により、それらの起源は2023年4月にアップロードされた2つのGeaconバリアントであるgeacon_plusとgeacon_proにさかのぼることができました。これらのツールは、匿名の中国人開発者であるz3ratu1とH4de5によって開発されました。また、geacon_proプロジェクトは現在GitHubで利用できず、2023年3月6日にキャプチャされたインターネットアーカイブスナップショットによって、Microsoft Defender、Kaspersky and Qihoo 360 360 Core Crystalなどのウイルス対策エンジンをバイパスする能力が示されていたことがわかりました。Geaconは、CobaltStrikeバージョン4.1以降をサポートするために開発されたと主張しており、現在のバージョンは4.8です。SentinelOneが発見したアーティファクトの1つであるXu Yiqing's Resume_20230320.appは、AppleScriptを使用してリモートサーバーに接続し、Geaconペイロードをダウンロードするように構成されています。また、Geaconバイナリには、さまざまな機能が詰め込まれており、次のステージのペイロードのダウンロードやデータの外部出力、ネットワーク通信の容易化を可能にします。SentinelOneが報告した2番目のサンプルは、Intelデバイスを標的とした、SecureLinkリモートサポートアプリ (SecureLink.app)を装ったトロイの木馬アプリケーションに埋め込まれています。このアプリケーションは、基本的には、連絡先、写真、リマインダー、およびデバイスのカメラとマイクにアクセスするための許可をユーザーに要求する非署名アプリケーションです。その主要なコンポーネントは、日本の既知のコマンドアンドコントロール（C2）サーバーに接続するGeaconペイロードであり、Geacon Proプロジェクトから構築されています。これに伴い、macOSエコシステムは、バックドアや情報スティーラーを展開するために、国家主導のグループを含む様々な脅威が標的になっています。SentinelOneの研究者は、「過去数か月間にGeaconサンプルが増加したことから、セキュリティチームはこのツールに注意を払い、適切な保護策を講じる必要がある」と結論づけています。",
        ),
    ]


@router.get("/news/{news_id}", response_model=news_schema.News)
async def detail_news():
    return news_schema.News(
        id=1,
        title="Cyolo 製品概要：すべての環境への安全なリモートアクセス",
        keywords={
            "OTセキュリティ": "オペレーションテクノロジーを守るために必要なセキュリティ対策",
            "ゼロトラスト": "アクセス許可において、信頼を前提にせずに認証を行うセキュリティアプローチ",
            "IdP": "ユーザーのアイデンティティを扱うサービス",
        },
        content="オペレーションテクノロジー（OT）のサイバーセキュリティは、組織の重要なシステムとリソースを保護するために必要不可欠ですが、複雑で困難な側面でもあります。最近は、サイバー犯罪者はシステムに突破するのではなくログインすることが多くなり、アクセスセキュリティがより複雑であるため管理と制御がますます重要になっています。このようなアクセス関連の課題に対処するために、Cyoloのチームは、OTおよび産業制御システム（ICS）環境の独自のセキュリティ、安全性、可用性要件を満たすゼロトラストアクセスプラットフォームを構築しています。\n\nCyoloのソリューションは、ゼロトラストネットワークアクセス（ZTNA）、Identity Provider（IdP）、Privileged Access Management（PAM）の組み合わせです。他のZTNAソリューションにはIdPまたはPAM機能がない一方、Identity and Access Managementツール（IdPとPAM）は接続性を拡張していません。Cyoloはクラウド接続またはエンドポイントエージェントのインストールを必要としないため、多くの組織が苦戦している接続性のユースケースに対処できます。 また、Cyoloは、Identity Access Controller（IDAC）とEdgeの組み合わせによって構築されており、IDACはTransport Layer Security（TLS）1.3接続を終了し、Cyolo管理者によって構成されたアクセスポリシーを強制します。IDACは逆プロキシとして機能し、すべての復号化と強制は組織のファイアウォールの後ろで行われます。EdgeはIDACに関連するSNIヘッダーに基づいてユーザーのリクエストをルーティングします。Edgeは、外部接続なしで動作することができ、トラフィックを傍受しないため、ゼロトラスト原則に準拠したまれなゼロトラストアクセスソリューションです。\n\nCyoloはオンプレミス、SaaSモデル、ハイブリッドの3つのデプロイメント方式に対応しています。必要に応じて完全に分離され、Non-IP接続されることができます。主要なコンポーネントとして、Identity providers（IdP）とIdentity Access Controller（IDAC）があります。Cyoloは既存のIdPと統合することができますし、CyoloのローカルIdPを使用することもできます。IDACはIdPに直接接続するため、Edge経由でアクセスする必要はありません。また、IDACには、ユーザーのセッションを接続するか、どの公開されたアプリケーションについてもアウトバウンド通信があるため、常にコミュニケーションが発生します。Cyoloは、一般的なIdPs（Okta、Active Directory、Azure AD、Pingなど）とも連携することができます。マルチファクタ認証（MFA）などの追加認証ステップを要求することもできます。\n\nCyoloは、有効なアイデンティティに基づいてすべてのアプリケーションに接続し、ユーザーのためにクレデンシャルを挿入して完全なシングルサインオン（SSO）エクスペリエンスを実現します。また、Cyoloはセキュリティアサーションマークアップ言語（SAML）やOpenID Connect（OIDC）で通信しない旧式の機器やシステム向けに、MFAおよびSSOを拡張することができます。各アプリケーションは、個々のユーザーやグループ、時間帯、場所などを考慮した特定のアクセスパラメータに設定されているため、必要な権限を持つユーザーにのみアクセスが許可されます。アクセスする前に承認を要求したり、各アクセスセッションを記録したりすることもできます。プラットフォーム上のすべてのアクティビティは、容易にエクスポート可能なログとして追跡されます。Cyoloは、ゲストアクセスの追加など、OT環境の調整が困難な状況に特に役立ちます。Cyoloを利用すると、クラウド接続を必要としないため、ネットワークの重要なセグメントを分離し、アクセスを制限する必要がある企業に最適です。また、Cyoloはエージェントのインストールが必要ないため、サードパーティ、外部の請負業者、またはビジネスパートナーに使用することが容易です。",
    )
