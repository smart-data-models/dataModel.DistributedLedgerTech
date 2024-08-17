from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    conint,
    constr,
)


class DltType(Enum):
    eth = 'eth'
    iota = 'iota'


class Logs(BaseModel):
    blockHash: Optional[str] = Field(
        None, description='Hash of the block where this log was in'
    )
    blockNumber: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The block number where this log was in. null when its pending. null when its pending log',
    )
    data: Optional[str] = Field(
        None,
        description='Contains one or more 32 Bytes non-indexed arguments of the log',
    )
    id: Optional[str] = Field(None, description='Log id')
    logAddress: Optional[str] = Field(
        None, description='Address from which this log originated'
    )
    logIndex: Optional[confloat(ge=0.0)] = Field(
        None,
        description=' Integer of the log index position in the block. null when its pending log',
    )
    removed: Optional[bool] = Field(
        None,
        description='True when the log was removed, due to a chain reorganization. False if its a valid log',
    )
    topics: Optional[List[str]] = Field(
        None,
        description='Array of 0 to 4 32 Bytes DATA of indexed log arguments. (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)',
    )
    transactionHash: Optional[str] = Field(
        None,
        description='Hash of the transactions this log was created from. null when its pending log',
    )
    transactionIndex: Optional[confloat(ge=0.0)] = Field(
        None,
        description=' Integer of the transactions index position log was created from. null when its pending log',
    )


class StorageType(Enum):
    iota = 'iota'
    ipfs = 'ipfs'
    merkletree = 'merkletree'


class TxReceipts(BaseModel):
    blockHash: Optional[str] = Field(
        None, description='Hash of the block of the transaction'
    )
    blockNumber: Optional[conint(ge=0)] = Field(
        None, description='Block number of the transaction'
    )
    contractAddress: Optional[str] = Field(
        None,
        description='Contract address created, if the transaction was a contract creation, otherwise null',
    )
    cumulativeGasUsed: Optional[conint(ge=0)] = Field(
        None,
        description='Total amount of gas used when this transaction was executed in the block',
    )
    dltType: Optional[DltType] = Field(
        None, description="Enum:'eth, iota'. type of DLT used by the transaction"
    )
    from_: Optional[str] = Field(
        None,
        alias='from',
        description='Account Address of the user/service responsible to submit the transaction (address of the msg.sender)',
    )
    gasUsed: Optional[conint(ge=0)] = Field(
        None, description='The amount of gas used by this specific transaction'
    )
    keys: Optional[List[str]] = Field(
        None, description='Payload keys used in transaction payload'
    )
    logs: Optional[Logs] = Field(
        None,
        description='A log record can be used to describe an event within a smart contract (Ethereum)',
    )
    logsBloom: Optional[str] = Field(
        None,
        description='256 Bytes-bloom filter for light clients to quickly retrieve related logs',
    )
    objectType: Optional[str] = Field(
        None, description='Type of object has been persisted'
    )
    status: Optional[bool] = Field(
        None,
        description='True or False — which informs us if the txn was reverted or not — in this case it was true (0x1)',
    )
    storageType: Optional[StorageType] = Field(
        None,
        description="Enum:'iota, ipfs, merkletree'. Type of storage used to persist payload",
    )
    to: Optional[str] = Field(
        None,
        description='Account or Contract Address to transaction has been submitted',
    )
    transactionHash: Optional[str] = Field(None, description='Hash of the transaction')
    transactionIndex: Optional[conint(ge=0)] = Field(
        None, description='Integer of the transactions index position in the block'
    )


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    DLTtxReceipt = 'DLTtxReceipt'


class DLTtxReceipt(BaseModel):
    TxReceipts: Optional[TxReceipts] = Field(None, description='Transaction Receipt')
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refEntity: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Entity persisted in the DLT')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NSGI Entity Type. it has to be DLTtxReceipt'
    )
