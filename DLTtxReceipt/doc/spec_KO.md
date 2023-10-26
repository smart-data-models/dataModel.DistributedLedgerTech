<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: DLTtxReceipt  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.DistributedLedgerTech/blob/master/DLTtxReceipt/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **트랜잭션의 일부 속성(키)을 저장하는 DLT 영수증에 대한 설명입니다**.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `TxReceipts[object]`: 거래 영수증  	- `blockHash[string]`: 트랜잭션 블록의 해시  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `blockNumber[integer]`: 트랜잭션의 블록 번호  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `contractAddress[string]`: 트랜잭션이 컨트랙트 생성인 경우 생성된 컨트랙트 주소, 그렇지 않으면 무효입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cumulativeGasUsed[integer]`: 해당 트랜잭션이 블록에서 실행되었을 때 사용된 총 가스 총량  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `dltType[string]`: Enum:'eth, iota'. 트랜잭션에서 사용하는 DLT 유형  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `from[string]`: 트랜잭션 제출을 담당하는 사용자/서비스의 계정 주소(메시지 발신자 주소)  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `gasUsed[integer]`: 이 특정 거래에서 사용한 가스 사용량  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `keys[array]`: 트랜잭션 페이로드에 사용되는 페이로드 키    
	- `logs[object]`: 로그 기록은 스마트 컨트랙트(이더리움) 내에서 이벤트를 설명하는 데 사용할 수 있습니다.    
	- `logsBloom[string]`: 라이트 클라이언트를 위한 256바이트 블룸 필터로 관련 로그를 빠르게 검색할 수 있습니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `objectType[string]`: 개체 유형이 지속되었습니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `status[boolean]`: True 또는 False - txn이 되돌렸는지 여부를 알려주는데, 이 경우 true(0x1)입니다.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
	- `storageType[string]`: Enum:'iota, ipfs, merkletree'. 페이로드를 유지하는 데 사용되는 스토리지 유형  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `to[string]`: 거래할 계정 또는 계약 주소가 제출되었습니다.  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `transactionHash[string]`: 트랜잭션 해시  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `transactionIndex[integer]`: 블록 내 트랜잭션 인덱스 위치의 정수입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refEntity[*]`: DLT에 지속된 엔티티  . Model: [http://schema.org/URL](http://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NSGI 엔티티 유형은 DLTtxReceipt여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DLTtxReceipt:    
  description: Description of a DLT receipt storing some of the attributes (keys) of a transaction.    
  properties:    
    TxReceipts:    
      description: Transaction Receipt    
      properties:    
        blockHash:    
          description: Hash of the block of the transaction    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        blockNumber:    
          description: Block number of the transaction    
          minimum: 0    
          type: integer    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        contractAddress:    
          description: 'Contract address created, if the transaction was a contract creation, otherwise null'    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cumulativeGasUsed:    
          description: Total amount of gas used when this transaction was executed in the block    
          minimum: 0    
          type: integer    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        dltType:    
          description: 'Enum:''eth, iota''. type of DLT used by the transaction'    
          enum:    
            - eth    
            - iota    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        from:    
          description: Account Address of the user/service responsible to submit the transaction (address of the msg.sender)    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        gasUsed:    
          description: The amount of gas used by this specific transaction    
          minimum: 0    
          type: integer    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        keys:    
          description: Payload keys used in transaction payload    
          items:    
            type: string    
          type: array    
          x-ngsi:    
            type: Property    
        logs:    
          description: A log record can be used to describe an event within a smart contract (Ethereum)    
          properties:    
            blockHash:    
              description: Hash of the block where this log was in    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            blockNumber:    
              description: The block number where this log was in. null when its pending. null when its pending log    
              minimum: 0    
              type: number    
              x-ngsi:    
                model: https://schema.org/Number    
                type: Property    
            data:    
              description: Contains one or more 32 Bytes non-indexed arguments of the log    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            id:    
              description: Log id    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            logAddress:    
              description: Address from which this log originated    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            logIndex:    
              description: ' Integer of the log index position in the block. null when its pending log'    
              minimum: 0    
              type: number    
              x-ngsi:    
                model: https://schema.org/Number    
                type: Property    
            removed:    
              description: 'True when the log was removed, due to a chain reorganization. False if its a valid log'    
              type: boolean    
              x-ngsi:    
                model: https://schema.org/Boolean    
                type: Property    
            topics:    
              description: 'Array of 0 to 4 32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)'    
              items:    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            transactionHash:    
              description: Hash of the transactions this log was created from. null when its pending log    
              type: string    
              x-ngsi:    
                model: https://schema.org/Text    
                type: Property    
            transactionIndex:    
              description: ' Integer of the transactions index position log was created from. null when its pending log'    
              minimum: 0    
              type: number    
              x-ngsi:    
                model: https://schema.org/Number    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        logsBloom:    
          description: 256 Bytes-bloom filter for light clients to quickly retrieve related logs    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        objectType:    
          description: Type of object has been persisted    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        status:    
          description: True or False — which informs us if the txn was reverted or not — in this case it was true (0x1)    
          type: boolean    
          x-ngsi:    
            model: https://schema.org/Boolean    
            type: Property    
        storageType:    
          description: 'Enum:''iota, ipfs, merkletree''. Type of storage used to persist payload'    
          enum:    
            - iota    
            - ipfs    
            - merkletree    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        to:    
          description: Account or Contract Address to transaction has been submitted    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        transactionHash:    
          description: Hash of the transaction    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        transactionIndex:    
          description: Integer of the transactions index position in the block    
          minimum: 0    
          type: integer    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    refEntity:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Entity persisted in the DLT    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NSGI Entity Type. it has to be DLTtxReceipt    
      enum:    
        - DLTtxReceipt    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DistributedLedgerTech/blob/master/DLTtxReceipt/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/datamodel.DistributedLedgerTech/DLTtxReceipt/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### DLTtxReceipt NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 DLTtxReceipt의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
  "type": "DLTtxReceipt",  
  "refEntity": "urn:ngsi-ld:Animal:1",  
  "TxReceipts": {  
    "to": "0x9a3dbca554e9f6b9257aaa24010da8377c57c17e",  
    "from": "0x4c962a968ff8cc5c99688602969ada5caa3a92cb",  
    "keys": [  
      "id",  
      "type",  
      "species",  
      "legalId",  
      "birthdate",  
      "@context"  
    ],  
    "logs": {  
      "id": "log_e04a3da4",  
      "data": "0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000",  
      "topics": [  
        "0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175"  
      ],  
      "logAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
      "removed": false,  
      "logIndex": 0,  
      "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
      "blockNumber": 345522,  
      "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
      "transactionIndex": 0  
    },  
    "status": false,  
    "dltType": "eth",  
    "gasUsed": 112188,  
    "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
    "logsBloom": "0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000",  
    "objectType": "asset",  
    "blockNumber": 345522,  
    "storageType": "merkletree",  
    "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
    "contractAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
    "transactionIndex": 0,  
    "cumulativeGasUsed": 112188  
  },  
  "dateCreated": "2005-10-29T02:48:51Z",  
  "dateModified": "1980-07-30T13:43:48Z"  
}  
```  
</details>  
#### DLTtxReceipt NGSI-v2 정규화 예시  
다음은 정규화된 JSON-LD 형식의 DLTtxReceipt의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "VINF.36225393",  
  "type": "DLTtxReceipt",  
  "refEntity": {  
    "type": "Relationship",  
    "value": "Animal.1"  
  },  
  "TxReceipts": {  
    "type": "Property",  
    "value": {  
      "to": "0x9a3dbca554e9f6b9257aaa24010da8377c57c17e",  
      "from": "0x4c962a968ff8cc5c99688602969ada5caa3a92cb",  
      "keys": [  
        "id",  
        "type",  
        "species",  
        "legalId",  
        "birthdate",  
        "@context"  
      ],  
      "logs": {  
        "id": "log_e04a3da4",  
        "data": "0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000",  
        "topics": [  
          "0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175"  
        ],  
        "logAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
        "removed": false,  
        "logIndex": 0,  
        "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
        "blockNumber": 345522,  
        "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
        "transactionIndex": 0  
      },  
      "status": false,  
      "dltType": "eth",  
      "gasUsed": 112188,  
      "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
      "logsBloom": "0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000",  
      "objectType": "asset",  
      "blockNumber": 345522,  
      "storageType": "merkletree",  
      "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
      "contractAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
      "transactionIndex": 0,  
      "cumulativeGasUsed": 112188  
    }  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "1970-03-25T22:57:25Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2019-03-15T08:10:09Z"  
  }  
}  
```  
</details>  
#### DLTtxReceipt NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 DLTtxReceipt의 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
    "type": "DLTtxReceipt",  
    "TxReceipts": {  
        "to": "0x9a3dbca554e9f6b9257aaa24010da8377c57c17e",  
        "from": "0x4c962a968ff8cc5c99688602969ada5caa3a92cb",  
        "keys": [  
            "id",  
            "type",  
            "species",  
            "legalId",  
            "birthdate",  
            "@context"  
        ],  
        "logs": {  
            "id": "log_e04a3da4",  
            "data": "0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000",  
            "topics": [  
                "0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175"  
            ],  
            "logAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
            "removed": false,  
            "logIndex": 0,  
            "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
            "blockNumber": 345522,  
            "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
            "transactionIndex": 0  
        },  
        "status": false,  
        "dltType": "eth",  
        "gasUsed": 112188,  
        "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
        "logsBloom": "0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000",  
        "objectType": "asset",  
        "blockNumber": 345522,  
        "storageType": "merkletree",  
        "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
        "contractAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
        "transactionIndex": 0,  
        "cumulativeGasUsed": 112188  
    },  
    "dateCreated": "2005-10-29T02:48:51Z",  
    "dateModified": "1980-07-30T13:43:48Z",  
    "refEntity": "urn:ngsi-ld:Animal:1",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DistributedLedgerTech/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DLTtxReceipt NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 DLTtxReceipt의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:dataModel:id:VINF:36225393",  
    "type": "DLTtxReceipt",  
    "TxReceipts": {  
        "type": "Property",  
        "value": {  
            "to": "0x9a3dbca554e9f6b9257aaa24010da8377c57c17e",  
            "from": "0x4c962a968ff8cc5c99688602969ada5caa3a92cb",  
            "keys": [  
                "id",  
                "type",  
                "species",  
                "legalId",  
                "birthdate",  
                "@context"  
            ],  
            "logs": {  
                "id": "log_e04a3da4",  
                "data": "0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000",  
                "topics": [  
                    "0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175"  
                ],  
                "logAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
                "removed": false,  
                "logIndex": 0,  
                "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
                "blockNumber": 345522,  
                "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
                "transactionIndex": 0  
            },  
            "status": false,  
            "dltType": "eth",  
            "gasUsed": 112188,  
            "blockHash": "0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
            "logsBloom": "0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000",  
            "objectType": "asset",  
            "blockNumber": 345522,  
            "storageType": "merkletree",  
            "transactionHash": "0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
            "contractAddress": "0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
            "transactionIndex": 0,  
            "cumulativeGasUsed": 112188  
        }  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1970-03-25T22:57:25Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2019-03-15T08:10:09Z"  
        }  
    },  
    "refEntity": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Animal:1"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DistributedLedgerTech/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
