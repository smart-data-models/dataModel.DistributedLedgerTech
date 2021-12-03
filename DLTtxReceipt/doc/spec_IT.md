Entità: DLTtxReceipt  
====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.DistributedLedgerTech/blob/master/DLTtxReceipt/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Descrizione di una ricevuta DLT che memorizza alcuni degli attributi (chiavi) di una transazione.**  

## Elenco delle proprietà  

- `TxReceipts`: Ricevuta della transazione  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `refEntity`: Entità persistente nel DLT  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: NSGI Entity Type. deve essere DLTtxReceipt    
Proprietà richieste  
- `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DLTtxReceipt:    
  description: 'Description of a DLT receipt storing some of the attributes (keys) of a transaction.'    
  properties:    
    TxReceipts:    
      description: 'Transaction Receipt'    
      properties:    
        blockHash:    
          description: 'Property. Model:''https://schema.org/Text''. Hash of the block of the transaction'    
          type: string    
        blockNumber:    
          description: 'Property. Model:''https://schema.org/Number''. Block number of the transaction'    
          minimum: 0    
          type: integer    
        contractAddress:    
          description: 'Property. Model:''https://schema.org/Text''. Contract address created, if the transaction was a contract creation, otherwise null'    
          type: string    
        cumulativeGasUsed:    
          description: 'Property. Model:''https://schema.org/Number''. Total amount of gas used when this transaction was executed in the block'    
          minimum: 0    
          type: integer    
        dltType:    
          description: 'Property. Model:''https://schema.org/Text''. Enum:''eth, iota''. type of DLT used by the transaction'    
          enum:    
            - eth    
            - iota    
          type: string    
        from:    
          description: 'Property. Model:''https://schema.org/Text''. Account Address of the user/service responsible to submit the transaction (address of the msg.sender)'    
          type: string    
        gasUsed:    
          description: 'Property. Model:''https://schema.org/Number''. The amount of gas used by this specific transaction'    
          minimum: 0    
          type: integer    
        keys:    
          description: 'Property. Payload keys used in transaction payload'    
          items:    
            type: string    
          type: array    
        logs:    
          description: 'Property. A log record can be used to describe an event within a smart contract (Ethereum)'    
          properties:    
            blockHash:    
              description: 'Property. Model:''https://schema.org/Text''. Hash of the block where this log was in'    
              type: string    
            blockNumber:    
              description: 'Property. Model:''https://schema.org/Number''. The block number where this log was in. null when its pending. null when its pending log'    
              minimum: 0    
              type: integer    
            data:    
              description: 'Property. Model:''https://schema.org/Text''. Contains one or more 32 Bytes non-indexed arguments of the log'    
              type: string    
            id:    
              description: 'Property. Model:''https://schema.org/Text''. Log id'    
              type: string    
            logAddress:    
              description: 'Property. Model:''https://schema.org/Text''. Address from which this log originated'    
              type: string    
            logIndex:    
              description: 'Property. Model:''https://schema.org/Number''.  Integer of the log index position in the block. null when its pending log'    
              minimum: 0    
              type: integer    
            removed:    
              description: 'Property. Model:''https://schema.org/Boolean''. True when the log was removed, due to a chain reorganization. False if its a valid log'    
              type: boolean    
            topics:    
              description: 'Property. Array of 0 to 4 32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)'    
              items: {}    
              type: array    
            transactionHash:    
              description: 'Property. Model:''https://schema.org/Text''. Hash of the transactions this log was created from. null when its pending log'    
              type: string    
            transactionIndex:    
              description: 'Property. Model:''https://schema.org/Number''.  Integer of the transactions index position log was created from. null when its pending log.'    
              minimum: 0    
              type: integer    
          type: object    
        logsBloom:    
          description: 'Property. Model:''https://schema.org/Text''. 256 Bytes-bloom filter for light clients to quickly retrieve related logs'    
          type: string    
        objectType:    
          description: 'Property. Model:''https://schema.org/Text''. Type of object has been persisted'    
          type: string    
        status:    
          description: 'Property. Model:''https://schema.org/Boolean''. True or False — which informs us if the txn was reverted or not — in this case it was true (0x1)'    
          type: boolean    
        storageType:    
          description: 'Property. Model:''https://schema.org/Text''. Enum:''iota, ipfs, merkletree''. Type of storage used to persist payload'    
          enum:    
            - iota    
            - ipfs    
            - merkletree    
          type: string    
        to:    
          description: 'Property. Model:''https://schema.org/Text''. Account or Contract Address to transaction has been submitted'    
          type: string    
        transactionHash:    
          description: 'Property. Model:''https://schema.org/Text''. Hash of the transaction'    
          type: string    
        transactionIndex:    
          description: 'Property. Model:''https://schema.org/Number''. Integer of the transactions index position in the block'    
          minimum: 0    
          type: integer    
      type: object    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &dlttxreceipt_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *dlttxreceipt_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refEntity:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Entity persisted in the DLT'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NSGI Entity Type. it has to be DLTtxReceipt'    
      enum:    
        - DLTtxReceipt    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Esempio di payloads  
#### DLTtxReceipt NGSI-v2 valori chiave Esempio  
Ecco un esempio di un DLTtxReceipt in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### DLTtxReceipt NGSI-v2 normalizzato Esempio  
Ecco un esempio di un DLTtxReceipt in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### DLTtxReceipt NGSI-LD valori-chiave Esempio  
Ecco un esempio di un DLTtxReceipt in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
  "dateModified": "1980-07-30T13:43:48Z",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### DLTtxReceipt NGSI-LD normalizzato Esempio  
Ecco un esempio di un DLTtxReceipt in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id":"urn:ngsi-ld:dataModel:id:VINF:36225393",  
    "type":"DLTtxReceipt",  
    "refEntity":{  
        "type":"Relationship",  
        "object":"urn:ngsi-ld:Animal:1"  
    },  
    "TxReceipts":{  
        "type":"Property",  
        "value":{  
            "to":"0x9a3dbca554e9f6b9257aaa24010da8377c57c17e",  
            "from":"0x4c962a968ff8cc5c99688602969ada5caa3a92cb",  
            "keys":[  
                "id",  
                "type",  
                "species",  
                "legalId",  
                "birthdate",  
                "@context"  
            ],  
            "logs":{  
                "id":"log_e04a3da4",  
                "data":"0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000",  
                "topics":[  
                    "0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175"  
                ],  
                "logAddress":"0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
                "removed":false,  
                "logIndex":0,  
                "blockHash":"0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
                "blockNumber":345522,  
                "transactionHash":"0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
                "transactionIndex":0  
            },  
            "status":false,  
            "dltType":"eth",  
            "gasUsed":112188,  
            "blockHash":"0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56",  
            "logsBloom":"0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000",  
            "objectType":"asset",  
            "blockNumber":345522,  
            "storageType":"merkletree",  
            "transactionHash":"0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517",  
            "contractAddress":"0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e",  
            "transactionIndex":0,  
            "cumulativeGasUsed":112188  
        }  
    },  
    "dateCreated":{  
        "type":"Property",  
        "value":{  
            "@type":"DateTime",  
            "@value":"1970-03-25T22:57:25Z"  
        }  
    },  
    "dateModified":{  
        "type":"Property",  
        "value":{  
            "@type":"DateTime",  
            "@value":"2019-03-15T08:10:09Z"  
        }  
    },  
    "@context":[  
        "https://smartdatamodels.org/context.jsonld"  
    ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza