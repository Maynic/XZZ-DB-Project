/*!
  _   _  ___  ____  ___ ________  _   _   _   _ ___   
 | | | |/ _ \|  _ \|_ _|__  / _ \| \ | | | | | |_ _| 
 | |_| | | | | |_) || |  / / | | |  \| | | | | || | 
 |  _  | |_| |  _ < | | / /| |_| | |\  | | |_| || |
 |_| |_|\___/|_| \_\___/____\___/|_| \_|  \___/|___|
                                                                                                                                                                                                                                                                                                                                       
=========================================================
* Horizon UI - v1.1.0
=========================================================

* Product Page: https://www.horizon-ui.com/
* Copyright 2022 Horizon UI (https://www.horizon-ui.com/)

* Designed and Coded by Simmmple

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

// Chakra imports
import { Box, SimpleGrid } from "@chakra-ui/react";
import DataTable from "views/admin/StoreOrder/table";
import {
  columns,
} from "views/admin/StoreOrder/columns";

import React, { Component } from "react";

import axios from "axios";
import { API_URL, } from "constants";


class Onetable extends Component {
  state = {
    data: []
  };
  API_Ful = API_URL + "store_order";

  componentDidMount() {
    this.resetState();
  }

  getData = () => {
    axios.get(this.API_Ful).then(res => this.setState({ data: res.data }));
  };

  resetState = () => {
    this.getData();
  };

  render() {
    return (
      <Box pt={{ base: "130px", md: "80px", xl: "80px" }}>
        <SimpleGrid
          mb='20px'
          // columns={{ sm: 1, md: 2 }}
          spacing={{ base: "20px", xl: "20px" }}>
          <DataTable
            columnsData={columns}
            tableData={this.state.data}
            resetState={this.resetState}
          />

        </SimpleGrid>
      </Box>
    );
  }
}

export default Onetable;