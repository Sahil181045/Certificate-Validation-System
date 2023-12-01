// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Certification {
    struct Certificate {
        string uid;
        string candidate_name;
        string course_name;
        string org_name;
        string ipfs_hash;
    }

    mapping(string => Certificate) public certificates;
    event certificateGenerated(string certificate_id);

    function generateCertificate(
        string memory _certificate_id,
        string memory _uid,
        string memory _candidate_name,
        string memory _course_name,
        string memory _org_name,
        string memory _ipfs_hash
    ) public {
        // Check if certificate with the given ID already exists
        require(
            bytes(certificates[_certificate_id].ipfs_hash).length == 0,
            "Certificate with this ID already exists"
        );

        // Create the certificate
        Certificate memory cert = Certificate({
            uid: _uid,
            candidate_name: _candidate_name,
            course_name: _course_name,
            org_name: _org_name,
            ipfs_hash: _ipfs_hash
        });

        // Store the certificate in the mapping
        certificates[_certificate_id] = cert;

        // Emit an event
        emit certificateGenerated(_certificate_id);
    }

    function getCertificate(
        string memory _certificate_id
    )
        public
        view
        returns (
            string memory _uid,
            string memory _candidate_name,
            string memory _course_name,
            string memory _org_name,
            string memory _ipfs_hash
        )
    {
        Certificate memory cert = certificates[_certificate_id];

        // Check if the certificate with the given ID exists
        require(
            bytes(certificates[_certificate_id].ipfs_hash).length != 0,
            "Certificate with this ID does not exist"
        );

        // Return the values from the certificate
        return (
            cert.uid,
            cert.candidate_name,
            cert.course_name,
            cert.org_name,
            cert.ipfs_hash
        );
    }

    function isVerified(
        string memory _certificate_id
    ) public view returns (bool) {
        return bytes(certificates[_certificate_id].ipfs_hash).length != 0;
    }
}
