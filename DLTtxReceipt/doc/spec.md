<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: DLTtxReceipt  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.DistributedLedgerTech/blob/master/DLTtxReceipt/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Description of a DLT receipt storing some of the attributes (keys) of a transaction.**  
version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `TxReceipts[object]`: Transaction Receipt  	- `blockHash[string]`: Hash of the block of the transaction  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `blockNumber[integer]`: Block number of the transaction  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `contractAddress[string]`: Contract address created, if the transaction was a contract creation, otherwise null  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cumulativeGasUsed[integer]`: Total amount of gas used when this transaction was executed in the block  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `dltType[string]`: Enum:'eth, iota'. type of DLT used by the transaction  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `from[string]`: Account Address of the user/service responsible to submit the transaction (address of the msg.sender)  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `gasUsed[integer]`: The amount of gas used by this specific transaction  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `keys[array]`: Payload keys used in transaction payload    
	- `logs[object]`: A log record can be used to describe an event within a smart contract (Ethereum)    
	- `logsBloom[string]`: 256 Bytes-bloom filter for light clients to quickly retrieve related logs  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `objectType[string]`: Type of object has been persisted  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `status[boolean]`: True or False — which informs us if the txn was reverted or not — in this case it was true (0x1)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)  
	- `storageType[string]`: Enum:'iota, ipfs, merkletree'. Type of storage used to persist payload  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `to[string]`: Account or Contract Address to transaction has been submitted  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `transactionHash[string]`: Hash of the transaction  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refEntity[*]`: Entity persisted in the DLT  . Model: [http://schema.org/URL](http://schema.org/URL)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NSGI Entity Type. it has to be DLTtxReceipt  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### DLTtxReceipt NGSI-v2 key-values Example    
Here is an example of a DLTtxReceipt in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### DLTtxReceipt NGSI-v2 normalized Example    
Here is an example of a DLTtxReceipt in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### DLTtxReceipt NGSI-LD key-values Example    
Here is an example of a DLTtxReceipt in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### DLTtxReceipt NGSI-LD normalized Example    
Here is an example of a DLTtxReceipt in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
